const moveToNext = (array) => {
  const elementToMove = array.shift();
  array.push(elementToMove);
};

const moveToTargetAtDistance = (array, distanceToMove) => {
  let distanceLeftToMove = distanceToMove;
  while (distanceLeftToMove > 1) {
    moveToNext(array);
    distanceLeftToMove -= 1;
  }
};

const kill = (array) => {
  array.shift();
};

const execute = (subjects, killDistance) => {
  if (subjects.length === 1) {
    return null;
  }

  while (subjects.length > 1) {
    moveToTargetAtDistance(subjects, killDistance);
    kill(subjects);
  }

  return subjects[0];
};

module.exports = {
  execute,
  moveToNext,
  moveToTargetAtDistance,
  kill,
};
