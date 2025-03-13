function cleanSet(set, startString) {
const result = [];
for (let item of set) {
if (item.startsWith(startString)) {
result.push(item.slice(startString.length));
}
}
return result.join('-');
}

export default cleanSet;
