const magnusKata = (books) => {
  const bookCollections = [];

  books.map((book) => {
    const firstCollectionWithoutBook = bookCollections.find(
      collection => !collection.includes(book),
    );

    if (!firstCollectionWithoutBook) {
      bookCollections.push([book]);
    } else {
      firstCollectionWithoutBook.push(book);
    }
  });

  let cost = 0;
  bookCollections.map((collection) => {
    const booksInCollection = collection.length;
    switch (booksInCollection) {
      case 1:
        cost += 800;
        break;
      case 2:
        cost += (800 * 2) * 0.95;
        break;
      case 3:
        cost += (800 * 3) * 0.90;
        break;
      case 4:
        cost += (800 * 4) * 0.80;
        break;
      case 5:
        cost += (800 * 5) * 0.75;
        break;
      default:
        break;
    }
  });

  return cost;
};

module.exports = {
  magnusKata,
};
