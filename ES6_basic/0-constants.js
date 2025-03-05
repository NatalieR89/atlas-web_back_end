function taskFirst() {
    const task = 'I prefer const when I can.';
    return task;
  }
  
  function taskNext() {
    let task = 'But sometimes let is better.';
    return task;
  }

  module.exports = { taskFirst, taskNext };