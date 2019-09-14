const {
  execute, moveToNext, moveToTargetAtDistance, kill,
} = require('./executioner');

describe('execute', () => {
  it('should return no one if only one person is provided', () => {
    const subjects = ['bob'];
    const killDistance = 1;

    expect(execute(subjects, killDistance)).toBe(null);
  });

  it('should return the second person if two people are provided and the killDistance is 1', () => {
    const subjects = ['name1', 'name2'];
    const killDistance = 1;

    expect(execute(subjects, killDistance)).toBe('name2');
  });

  it('should return the last person if people are provided and the killDistance is 1', () => {
    const subjects = ['name1', 'name2', 'name3', 'name4', 'name5'];
    const killDistance = 1;

    expect(execute(subjects, killDistance)).toBe('name5');
  });

  it('should return the third person if people are provided and the killDistance is 2', () => {
    const subjects = ['name1', 'name2', 'name3', 'name4', 'name5'];
    const killDistance = 2;

    expect(execute(subjects, killDistance)).toBe('name3');
  });
});

describe('moveToNext', () => {
  it('should move the first item to the last item', () => {
    const array = [1, 2, 3, 4];
    moveToNext(array);

    expect(array[0]).toBe(2);
    expect(array[3]).toBe(1);
  });
});

describe('moveToTargetAtDistance', () => {
  it('should shift the array the distance provided', () => {
    const array = [1, 2, 3, 4];
    moveToTargetAtDistance(array, 2);

    expect(array[0]).toBe(2);

    moveToTargetAtDistance(array, 3);
    expect(array[0]).toBe(4);
  });
});

describe('kill', () => {
  it('removes the first element in an array', () => {
    const array = [1, 2, 3, 4];
    kill(array);

    expect(array[0]).toBe(2);

    kill(array);
    expect(array[0]).toBe(3);
  });
});
