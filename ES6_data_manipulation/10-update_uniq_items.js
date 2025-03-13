function updateUniqueItems(groceriesMap) {
  if (!(groceriesMap instanceof Map)) {
    throw new Error('Cannot process');
  }

  for (let [key, value] of groceriesMap) {
    if (value === 1) {
      groceriesMap.set(key, 100);
    }
  }
}

export default updateUniqueItems;
