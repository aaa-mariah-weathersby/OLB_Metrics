class CookieHelper {
  static getCookie(name, req) {
    if (req) {
      const cookie = req.cookies[name];
      return cookie || null;
    } else if (global.document) {
      const value = `; ${global.document.cookie}`;
      const parts = value.split(`; ${name}=`);
      if (parts.length === 2) return parts.pop().split(';').shift();
    }
    return null;
  }
}

export default CookieHelper;
