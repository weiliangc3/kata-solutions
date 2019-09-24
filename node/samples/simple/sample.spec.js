const sample = require('./sample').sample;

describe('sample', () => {
  it('should return input', () => {
    expect(sample('test')).toBe('test');
  });
});