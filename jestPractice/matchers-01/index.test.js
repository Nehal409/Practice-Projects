const add = require("./index");

describe("testing addition", () => {
  // Title of the test
  it("should add 1 + 4 to equal 5", () => {
    // calling function that should be tested
    const result = add(1, 4);

    // expected result
    expect(result).toBe(5);
  });

  it("obj shoould be equal to object", () => {
    const obj = {};
    expect(obj).toEqual({});
  });
});

describe("truthy or falsy", () => {
  it("null", () => {
    const n = null;
    // expect(n).not.toBeFalsy()
    // expect(n).toBeFalsy()
    expect(n).toBeNull();
  });
});

describe("numbers", () => {
  it("two plus two", () => {
    const value = 2 + 2;
    expect(value).toBe(4);
    expect(value).toBeGreaterThan(3);
    expect(value).toBeGreaterThanOrEqual(4);
    expect(value).toBeLessThan(5);
    expect(value).toBeLessThanOrEqual(4);
  });

  it("adding floats", () => {
    const value = 0.1 + 0.2;
    expect(value).toBeCloseTo(0.299999399);
  });
});

describe("strings", ()=>{
  it("there is no i in team", ()=>{
    expect("team").not.toMatch(/I/)
  })
})

describe("arrays", ()=>{
  it("testing arrays", ()=>{
    const shoppingList = [
      'soda','pepsi','cocacola','milk'
    ]
    expect(shoppingList).toContain('milk')
  })
})

function compileAndroidCode(){
  throw new Error("Error Occured!!!")
}
// Error handling
describe("exceptions", ()=>{
  it("using exceptions", ()=>{
    expect(()=> compileAndroidCode()).toThrow(Error)
  })

})
