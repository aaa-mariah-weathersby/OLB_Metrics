var gulp = require("gulp"),
grepc = require("gulp-grep-contents"),
gprint = require("gulp-print"),
change = require("gulp-change");

const specpath = 'specs/';
const specfilepath = specpath + '**/*.spec.js';

gulp.task('find-only', function(){
	return gulp.src(specfilepath)
	.pipe(grepc( /\.only\(/))
	.pipe(gprint());
});

gulp.task('find-skip', function(){
	return gulp.src(specfilepath)
	.pipe(grepc( /\.skip\(/))
	.pipe(gprint());
});

gulp.task('rm-only', function(){
	function removeOnly(content){
		return content.replace(/\.only\(/, '(');
	}
	
	return gulp.src(specfilepath)
	.pipe(grepc( /\.only\(/))
	.pipe(gprint())
	.pipe(change(removeOnly))
	.pipe(gulp.dest(specpath));
});
