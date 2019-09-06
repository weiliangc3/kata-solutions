// Solution is incomplete. Mostly created just to play around with reducers.

const magnusKata = (books) => {
  const sortedBooks = books.sort();

  const bookArray = sortedBooks.reduce((total, book, currentIndex) => {
    const arrayToWorkOn = currentIndex === 1 ? [[book]] : total
    lastBookArray = arrayToWorkOn[arrayToWorkOn.length - 1];

    if (lastBookArray.includes(book)) {
      arrayToWorkOn.push([book]);

      return arrayToWorkOn
    }
    lastBookArray.push(book)
    return arrayToWorkOn;
  })

  if(books.length > 1 && books[0] != books[1]) {
    return 800 * books.length * 0.95
  }
  return 800*books.length;

  // for (i in books) {
  //     discountBooks = []
  //     booksLeft = []
  //     if (discountBooks.includes(i)) {
  //       booksLeft = books.splice(books.indexOf(i))
  //       break
  //     } 
  //     discountBooks.push(i)

  // }

  const result = [[0,1],[0]]

//   console.log(discountBooks)

//   return (discountBooks.length * 800 * 0.95) + (booksLeft * 800);
  
  
}

module.exports = {
  magnusKata
};
