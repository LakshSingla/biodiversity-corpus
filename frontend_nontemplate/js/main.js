const mainCategorySelectElem = document.getElementById('main-category-select');
const subCategorySelectOuterElem = document.getElementById('subcategory-select-outer');

const mapping = {
    flora: ['Lily', 'Dahlia'],
    fauna: ['Tiger', 'Bear'],
    hills: ['Rugged'],
}

const getMainCategoryValue = () => mainCategorySelectElem.value;
const getSubCategoryValue = () => subCategorySelectElem.value;

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

    populateSubcategorySelect();
    initMap();
});

mainCategorySelectElem.addEventListener('change', populateSubcategorySelect);