//! Colas en js

var Queue = {
  items: [],
  limit: 10,

  Add: function (e) {
    //Agrega elementos Según el limite indicado
    return this.items.length < this.limit
      ? (this.items.push(e), 'agregado')
      : 'no se puede agregar elemento por que excede el limite permitido';
  },
  Offer: function (index, element) {
    //Agrega elementos dada una posición
    return this.items.length < this.limit
      ? ((this.items[index] = element), 'agregado')
      : 'no se puede agregar elemento por que excede el limite permitido';
  },
  Elements: function (limit) {
    //Muestra el número de elemtos contenidos según petición
    return this.items.length < limit
      ? 'la solicitud excede al tamaño del arreglo'
      : this.items.slice(0, limit);
  },
  Resum: function () {
    //muestra el primer , el ultimo elemento y el tamaño total del arreglo
    return this.items.length == 0
      ? 'no hay elementos'
      : `primer elemento es: ${
          this.items[0]
        },\n último elemento es: ${this.items.pop()},\n tamaño total del arreglo es: ${
          this.items.length
        }`;
  },
  Peek: function () {
    //muestra el primer elemento del arreglo
    return this.items.length == 0 ? 'no hay elementos' : this.items[0];
  },
  Poll: function () {
    //eliminar el primer elemento del arreglo
    return this.items.length == 0 ? 'no hay elementos' : this.items.shift();
  },
  Remove: function () {
    //eliminar el primer elemento del arreglo
    return this.items.shift();
  },
  Size: function () {
    return this.items.length;
  },
  Is_empty: function () {
    return this.items.length == 0;
  },
};

var Q = Queue;
console.log(Q);
console.log(Q.Peek());
console.log(Q.Add(1));
console.log(Q.Add(2));
console.log(Q.Add(4));
console.log(Q.Add(5));
console.log(Q.Offer(2, 3));
console.log(Q.Elements());
console.log(Q.Is_empty());
console.log(Q.Size());
console.log(Q.Peek());
console.log(Q.Elements());
console.log(Q.Poll());
console.log(Q.Elements());
console.log(Q.Remove());
console.log(Q.Elements());
console.log(Q.Resum());
console.log(Q.Size());
console.log(Q.Is_empty());
