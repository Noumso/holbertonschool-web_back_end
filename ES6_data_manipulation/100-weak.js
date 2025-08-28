export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (typeof endpoint !== 'object' || endpoint === null) {
    throw new TypeError('Endpoint must be a non-null object');
  }

  let called = weakMap.get(endpoint) || 0;

  called += 1;

  weakMap.set(endpoint, called);

  if (called >= 10) {
    throw Error('Endpoint load is high');
  }

  return called;
}