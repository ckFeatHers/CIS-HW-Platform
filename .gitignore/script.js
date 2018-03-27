/*
MidTerm Rework

*/

const message = document.querySelector('.show');
const message2 = document.querySelector('.show2');
message.textContent = "MidTerm Rework";
message2.textContent = "Wondering your average?";

/**
 * Returns random value
 * @param {number} min
 * @param {number} max
 * @return {number} Random number between min and max
 */
function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //The maximum is inclusive and the minimum is inclusive 
}

/**
 * Returns the Curve Score based on curveAmount 
 * @param {number} original
 * @param {number} curveAmount
 * @return {number} Curved Score
 */
function curveScore(original, curveAmount){
  return original + curveAmount;
}

//Put values into array - array is const but values can change

const testScores = Array.from({length:20}, () => getRandomIntInclusive(60,100));

//console.log(testScores); //original values for testing

testScores.forEach((eachScore, i, holdingArray) => {holdingArray[i] = curveScore(eachScore, 10)});

message.textContent = testScores;

/**
 * Returns the Curve Score based on curveAmount 
 * @param {number} array
 * @return {number} average of scores
 */

function getAverage(scores) {
    let total = 0; //declaring and initializing accumulator
    for(i = 0; i < scores.length; i++)
    {
      total += scores[i];     
      //total += testScores[i];
    }
   return total/scores.length;
    }
  
  let average = getAverage(testScores);
  
  message2.textContent = `Your average score with the curve is ${average}%.`;


 /////////////////////////////////////////////////////

 //refernces sites:
 
//reference http://usejsdoc.org/tags-returns.html

// reference https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random

//video reference https://manavm1990.github.io/javascript/arrays/2018/03/20/exam-rework.html
//reference https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from
//console.log(Array.from([1, 2, 3], x => x + x));
// expected output: Array [2, 4, 6]

//reference https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach
//function logArrayElements(element, index, array) {
//  console.log('a[' + index + '] = ' + element); }