export default function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      const rm = true;
      if (rm) {
        resolve();
      } else {
        reject();
      }
    });
  }

