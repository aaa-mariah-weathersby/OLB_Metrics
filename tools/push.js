import GitRepo from 'git-repository';
import child from 'child_process';
import fs from 'fs';

const exec = (command, args, options) => new Promise((resolve, reject) => {
  let out = '';
  let err = '';
  const p = child.spawn(command, args, options);
  p.stdout.on('data', data => out += data);
  p.stderr.on('data', data => err += data);
  p.on('error', reject);
  p.on('close', (code) => resolve([code, out.trim(), err.trim()]));
});

async function hasRef(repository, ref) {
  const opts = { cwd: 'build' };
  const [code, , err] = await exec('git', ['ls-remote', repository, ref, '--exit-code'], opts);
  if (code === 2) {
    return false;
  } else if (code === 0) {
    return true;
  }
  throw new Error(err);
}

async function checkout(branch) {
  const opts = { cwd: 'build' };
  const [code, , err] = await exec('git', ['checkout', branch], opts);
  if (code === 2) {
    return false;
  } else if (code === 0) {
    return true;
  }
  throw new Error(err);
}

function branch() {
  if (!process.env.NODE_ENV) {
    return 'acceptance';
  }

  if (process.env.NODE_ENV === 'production') {
    return 'master';
  }

  return process.env.NODE_ENV;
}

function environment() {
  if (!process.env.NODE_ENV) {
    return 'acceptance';
  }

  return process.env.NODE_ENV;
}

const remote = {
  name: 'app',
  url: 'git@github.com:clublabs/AppDeploy.git',
  branch: branch(),
};

function run(cmd) {
  console.log('Running build:', cmd);
  return new Promise((resolve, reject) => {
    child.exec(`npm run ${cmd}`, (error, stdout) => {
      if (error) {
        console.error(`exec error: ${error}`);
        reject(error);
      }
      resolve(stdout);
    });
  });
}

function copyMyFile(src,dst) {
  const sdata = fs.readFileSync(src, 'utf-8');
  fs.writeFileSync(dst, sdata);
}

async function push(msg) {
  const commitMessage = msg || 'Update';
  console.log('PUSH: *** START ***');
  console.log('Push started. Message:', commitMessage);
  console.log('Remote name:', remote.name);
  console.log('Remote branch:', remote.branch);
  await run('clean');
  const buildDir = 'build';

  if (!fs.existsSync(buildDir)) {
    fs.mkdirSync(buildDir);
  }
  let repo;
  const doGit = !process.env.IGNORE_GIT;
  
  try {
    if (doGit) {
      repo = await GitRepo.open(buildDir, { init: true });
      await repo.setRemote(remote.name, remote.url);
      if (await hasRef(remote.url, remote.branch)) {
        await repo.fetch(remote.name);
        await checkout(remote.branch);
      }
    }
    await run(`build:${environment()}`);

    const env = environment();

    const fileName = "ecosystem." + env + ".json";
    copyMyFile('server/' + fileName, 'build/' + fileName);

    if(env == 'production'){
      copyMyFile('server/ecosystem.prestage.json', 'build/ecosystem.prestage.json');
      copyMyFile('server/ecosystem.stage.json', 'build/ecosystem.stage.json');
    }

    if (doGit) {
      await repo.add('--all .');
      await repo.commit(commitMessage);
      await repo.push(remote.name, remote.branch, { force: true });
    }
  } catch (e) {
    console.error('!!!! error in fetch files from repo', e);
  }
  console.log('PUSH: *** END ***');
}

push();
