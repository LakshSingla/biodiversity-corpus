const mainCategorySelectElem = document.getElementById('main-category-select');
const mainCategorySelectOuterElem = document.getElementById('main-category-select-outer');
const subCategorySelectOuterElem = document.getElementById('subcategory-select-outer');
const searchBtn = document.getElementById('search-btn');

let g_map;          //Global variable for map
let g_codebird;     //Global variable for CodeBird

let mapping = {};

const getMainCategoryValue = () => mainCategorySelectOuterElem.querySelector('select').value;
const getSubCategoryValue = () => subCategorySelectElem.value;

const populateCategorySelect = () => {
    const _mainCategorySelectElem = mainCategorySelectOuterElem.querySelectorAll('.select-wrapper');
    _mainCategorySelectElem.forEach(elem => elem.remove())
    const selectElem = document.createElement('select');
    const elemArr = [];
    for(const k in mapping) {
        const elem = document.createElement('option');
        elem.setAttribute('value', k);
        elem.appendChild(document.createTextNode(k));
        elemArr.push(elem);
    }
    selectElem.addEventListener('change', populateSubcategorySelect);
    elemArr.forEach(elem => selectElem.appendChild(elem))
    mainCategorySelectOuterElem.prepend(selectElem);
    let elems = document.querySelectorAll('select');
    let selectInstances = M.FormSelect.init(elems, {});
}

const populateSubcategorySelect = () => {
    const subCategorySelectElem = subCategorySelectOuterElem.querySelectorAll('.select-wrapper');
    subCategorySelectElem.forEach(elem => elem.remove())
    const mainCategoryValue = getMainCategoryValue();
    const selectElem = document.createElement('select');
    mapping[mainCategoryValue].map(value => {
        const elem = document.createElement('option');
        elem.setAttribute('value', value);
        elem.appendChild(document.createTextNode(value));
        return elem;
    }).forEach(elem => selectElem.appendChild(elem));
    subCategorySelectOuterElem.prepend(selectElem);
    let elems = document.querySelectorAll('select');
    let selectInstances = M.FormSelect.init(elems, {});
}

document.addEventListener('DOMContentLoaded', () => {
    let elems;

    elems = document.querySelectorAll('select');
    let selectInstances = M.FormSelect.init(elems, {});

    elems = document.querySelectorAll('.datepicker');
    let datepickerInstances = M.Datepicker.init(elems, {
        showClearBtn: true
    });

    elems = document.querySelectorAll('.modal');
    let modalInstances = M.Modal.init(elems, {});

    // populateCategorySelect();
    // populateSubcategorySelect();

    fetch('/db/categories').then(data => data.json()).then(data => {
        console.log(data)
        mapping = data;
        populateCategorySelect();
        populateSubCategorySelect();
    })

    g_map = initMap();

    g_codebird = setupCodebird();
});

// mainCategorySelectElem.addEventListener('change', populateSubcategorySelect);
searchBtn.addEventListener('click', () => {
    g_codebird.__call('search_tweets', {
        q: getSubCategoryValue()
    }, result => {
        console.log(result)
    })

})
