const { sum } = require('../src/math');

test('adds numbers correctly', () => {
  expect(sum(2, 3)).toBe(5);
});
