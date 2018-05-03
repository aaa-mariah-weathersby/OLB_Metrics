import CookieHelper from '../../src/utils/cookieHelper';

class HttpDispatcher {
  processRequest(url, options, async) {
    const updatedOptions = { ...options };
    if (options.method === 'POST') {
      const csrft = CookieHelper.getCookie('csrft');
      if (csrft) {
        updatedOptions.headers['x-csrf-token'] = csrft;
        updatedOptions.credentials = 'include';
      }
    }

    const promise = fetch(url, updatedOptions);
    if (async) return promise;

    return promise.then(response => {
      return response.json().then(json => {
        return response.ok ? json : Promise.reject(json);
      });
    });
  }
}
export default HttpDispatcher;
