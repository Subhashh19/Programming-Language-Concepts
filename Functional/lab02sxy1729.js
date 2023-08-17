//Name: Sai Subhash Yalamadala 
//UTA ID: 1002031729
//Date: 28 June 2023 


//Q1. Inputtable array with numbers between 1 and 10.

const inputtable = [1,2,3,4,5,6,7,8,9,10];
console.log("1. Array",inputtable);

//2a. Set of multiples of 5 between 1 and 51.

// Create an array of numbers from 1 to 51
const numbers = Array.from({ length: 51 }, (_, i) => i + 1);

// Using filter() method to get the multiples of 5
const fiveTable = numbers.filter((number) => number % 5 === 0);

// Output the multiples of 5
console.log("2a. Multiples of 5 between 1 and 51:", fiveTable);


//2b. Set of multiples of 13 between 1 and 131.

// Create an array of numbers from 1 to 131
const numbers2 = Array.from({ length: 131 }, (_, i) => i + 1);

// Using filter() method to get the multiples of 13
const thirteenTable = numbers2.filter((number) => number % 13 === 0);
console.log("2b. Multiples of 13 between 1 and 131:", thirteenTable);


//2c. Set of squares of the numbers in inputtable (squaresTable).

// Using map() method to calculate the squares
const squaresTable = inputtable.map((number) => number * number);
console.log("2c. Squares of the numbers in inputTable:", squaresTable);


//Q3. Get the odd multiples of 5 between 1 and 100.

// Create an array of numbers from 1 to 100
const numbers3 = Array.from({ length: 100 }, (_, i) => i + 1);

// Using filter() method to get the odd multiples of 5
const oddMultiples = numbers3.filter((number) => number % 5 === 0 && number % 2 !== 0);
console.log("3. Odd multiples of 5 between 1 and 100:", oddMultiples);


//Q4. Get the sum of even multiples of 7 between 1 and 100.

// Create an array of numbers from 1 to 100
const numbers4 = Array.from({ length: 100 }, (_, i) => i + 1);

// Using filter() method to get the even multiples of 7
const evenMultiplesOfSeven = numbers4.filter((number) => number % 7 === 0 && number % 2 === 0);

// Using reduce() method to calculate the sum of even multiples of 7
const sum = evenMultiplesOfSeven.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
console.log("\n4. Sum of even multiples of 7 between 1 and 100:", sum);


//Q5. Rewrite the cylinder_volume function using currying.

const cylinder_volume = (r) => (h) => {
  const volume = 3.14 * r * r * h;
    return volume;
};

const cVolume = cylinder_volume(5);
//a. Call the curried function with r = 5 and h = 10
const volumeA = cVolume(10);
console.log("\n5a. Volume for r = 5 and h = 10:", volumeA);

//b. Reuse the function with h = 17
const volumeB = cVolume(17);
console.log("5b. Volume for h = 17:", volumeB);

//c. Reuse the function with h = 11
const volumeC = cVolume(11);
console.log("5c. Volume for h = 11:", volumeC);


//Q6. HTML 

const makeTag = function(beginTag, endTag) {
  return function(textContent) {
    return beginTag + textContent + endTag;
  };
};

const tableData = [
  ["Firstname", "Lastname", "Age"],
  ["Subhash", "Yalamadala", "25"],
  ["Mohan", "Bhoopathi", "25"],
  ["Michael", "Jordan", "60"]
];

const tableRowTags = makeTag("<tr>", "</tr>");
const tableHeaderTags = makeTag("<th>", "</th>");
const tableCellTags = makeTag("<td>", "</td>");

const tableRows = tableData.map(function(row) {
  if (row.includes("Firstname")) {
    return tableRowTags(row.map(tableHeaderTags).join(""));
  } else {
    return tableRowTags(row.map(tableCellTags).join(""));
  }
});

const table = makeTag("\n6. <table>\n", "</table>\n")(tableRows.join("\n"));
console.log(table);


//Q7. Create a generic function for finding multiples.

const findMultiples = (multiple, isOdd) => {
  const numbers = Array.from({ length: 100 }, (_, i) => i + 1);
  const multiples = numbers.filter(number => number % multiple === 0 && (isOdd ? number % 2 !== 0 : number % 2 === 0));
  const sum = multiples.reduce((total, number) => total + number, 0);
  return { multiples, sum };
};

const oddMultiplesOfEleven = findMultiples(11, true);
console.log("7. Odd multiples of 11 between 1 and 100:", oddMultiplesOfEleven);

const evenMultiplesOfThree = findMultiples(3, false);
console.log("   Even multiples of 3 between 1 and 100:", evenMultiplesOfThree);
