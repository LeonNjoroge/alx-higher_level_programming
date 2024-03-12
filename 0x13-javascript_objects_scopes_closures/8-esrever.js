#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let m = 0;
  while ((len - m) > 0) {
    const aux = list[len];
    list[len] = list[i];
    list[m] = aux;
    m++;
    len--;
  }

  return list;
};
