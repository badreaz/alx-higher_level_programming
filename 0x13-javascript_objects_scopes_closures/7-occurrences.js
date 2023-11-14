#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
  let nb = 0;
  list.map((item) => {
    if (item === searchElement) {
      nb++;
    }
    return (nb);
  });
  return (nb);
};
