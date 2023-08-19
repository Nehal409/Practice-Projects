const body = document.body;

/** Append Strings with append() to add to our webpage */
// body.append("hello nehal", " " ,"nasir khan");

/** Create elements and then Append */
// const div = document.createElement('div');

/** Modifying element text */
// const div = document.querySelector('div')
// console.log(div.textContent);
// console.log(div.innerText);

/** Render text inside an element */
// div.innerText = "hello"

/** Render Html code inside an element */
// div.innerHTML = "<b>bye bye</b>"

/** Doing work of innerHtml in a safer way, we broke it out and wrote the js by hand */
// const strong = document.createElement("strong")
// const text = "hello 2"
// strong.innerText = text
// div.append(strong)

const div =  document.querySelector('div')
const hi = document.querySelector('#hi')
const bye = document.querySelector('#bye')

/** Removing elements from the DOM */
// bye.remove()
/** Also we can remove from the parent */
// div.removeChild(hi)

/** Modifying attributes of a element */
// console.log(hi.getAttribute('title'));

// console.log(hi.setAttribute('title','nehal-nasir-khan'));

/** Remove attribute from a element */
// hi.removeAttribute('title');

/** Modifying elememt classes */
// bye.classList.add('new-class')
// bye.classList.remove('bye1')
/** It is going to remove the class if it exist and if it doesnot exist it will add that class */
// bye.classList.toggle('bye3')

/** Modifying style property of a element */
// bye.style.color = 'red'
// bye.style.backgroundColor = 'purple'
// bye.style.fontSize = '25px'

const array1 = [2,4,5,6,7]
const array2 = [2,4,5,6,7]

const numberMUltiplyByTwo = array1.map((data)=>
    data * 2
)

const numberMUltiplyTwo = array2.forEach((data)=>
    data * 2
)

console.log("Map function",numberMUltiplyByTwo);
console.log("forEach function",numberMUltiplyTwo);

body.append(div);


























