const magnusKata = require('./mapSolution').magnusKata;

describe('magnus kata tests', () => {
  it('should sum total one book', () => {
    books = [0]

    expect(magnusKata(books)).toBe(800);
  });

  it('has the right values for each book', () => {
    expect(magnusKata([0])).toBe(800);
    expect(magnusKata([1])).toBe(800);
    expect(magnusKata([2])).toBe(800);
    expect(magnusKata([3])).toBe(800);
    expect(magnusKata([4])).toBe(800);
  });

  it('returns the right value for multiple books of the same type', () => {
    books = [0,0,0]

    expect(magnusKata(books)).toBe(2400);
  });

  it('applies a 5% discount to the books when 2 different books are sold', () => {
    books = [0,1]

    expect(magnusKata(books)).toBe(1520);
  });

  it('applies a 5% discount to only the books that are different when multiple books are sold ', () => {
    books = [0,1,0]

    expect(magnusKata(books)).toBe(2320);
  });


  it('applies a 25% discount to the 5 books to only the books that are different when multiple books are sold ', () => {
    books = [2,1,2,3,4,0]

    expect(magnusKata(books)).toBe(3800);
  });
});