let NO_OF_PROJECT = 1
let NO_OF_EDUCATION = 1
let NO_OF_EXPERIENCE = 1


const executeFunctions = () => {
    loadDataFromLocalStorage()
}

const loadDataFromLocalStorage = () => {
    for (const key in localStorage) {
        // Skip built-in properties like length, setItem, etc.
        if (localStorage.hasOwnProperty(key)) {
            let targetInput = document.getElementById(`${key}`)
            targetInput.value = localStorage.getItem(key)
        }
    }
}

/* ----------------------
EVENT HANDLER HELPER FUNCTIONS
-------------------------*/

function setAttributes(el, options) {
    Object.keys(options).forEach(function (attr) {
        el.setAttribute(attr, options[attr]);
    })
}

const elementCreation = (element, classes = [], attributes = {}, inner_text = '', inner_html = '') => {
    let new_element = document.createElement(element)
    new_element.classList.add(...classes)
    setAttributes(new_element, attributes)
    new_element.innerText = inner_text
    if (inner_html !== '') {
        new_element.innerHTML = inner_html
    }
    return new_element
}

const formCreationHelper = (id) => {
    let data_object = {}
    if (id == 'add-project') {
        NO_OF_PROJECT = NO_OF_PROJECT + 1
        data_object = {
            'close_class': 'project-section-close',
            // second
            'title_label': 'Project Title',
            'title_input_id': `project-title-${NO_OF_PROJECT}`,
            // third div
            'tech_label': 'Tech Used',
            'tech_input_id': `project-tech-${NO_OF_PROJECT}`,
            // fourth div 
            'live_demo_input_id': `project-live-link-${NO_OF_PROJECT}`,
            'live_demo_label': 'Live Demo Link',

            'source_input_id': `project-source-code-${NO_OF_PROJECT}`,
            'source_label': 'Source Code',

            'start_input_id': `project-start-date-${NO_OF_PROJECT}`,
            // fifth div
            'end_input_id': `project-end-date-${NO_OF_PROJECT}`,
            'checkbox_input_id': `project-check-box-${NO_OF_PROJECT}`,
            'checkbox_label': 'On-going project',
            // sixth div
            'summary_label': 'Project Summary',
            'summary_input_id': `project-summary-${NO_OF_PROJECT}`,
            // section id
            'section_id': 'project-section',
        }
    }
    else if (id == 'add-education') {
        NO_OF_EDUCATION = NO_OF_EDUCATION + 1
        data_object = {
            'close_class': 'education-section-close',
            // second div
            'title_label': 'School/College',
            'title_input_id': `school-${NO_OF_EDUCATION}`,

            'tech_label': 'Degree',
            'tech_input_id': `degree-${NO_OF_EDUCATION}`,
            // fourth div 
            'live_demo_label': 'Subject',
            'live_demo_input_id': `education-subject-${NO_OF_EDUCATION}`,

            'source_label': 'Location',
            'source_input_id': `education-location-${NO_OF_EDUCATION}`,

            'start_input_id': `education-start-date-${NO_OF_EDUCATION}`,
            // fifth div
            'end_input_id': `education-end-date-${NO_OF_EDUCATION}`,
            'checkbox_input_id': `education-check-box-${NO_OF_EDUCATION}`,
            'checkbox_label': 'Not completed yet',
            // sixth div
            'summary_label': 'Summary',
            'summary_input_id': `education-summary-${NO_OF_EDUCATION}`,
            // section id
            'section_id': 'education-section',
        }
    }
    else if (id == 'add-experience') {
        NO_OF_EXPERIENCE = NO_OF_EXPERIENCE + 1
        data_object = {
            'close_class': 'experience-section-close',
            // second div
            'title_label': 'Company',
            'title_input_id': `company-${NO_OF_EXPERIENCE}`,

            'tech_label': 'Role',
            'tech_input_id': `role-${NO_OF_EXPERIENCE}`,
            // fourth div 
            'live_demo_label': 'Location',
            'live_demo_input_id': `experience-location-${NO_OF_EXPERIENCE}`,

            'source_label': 'Department',
            'source_input_id': `experience-dept-${NO_OF_EXPERIENCE}`,

            'start_input_id': `experience-start-date-${NO_OF_EXPERIENCE}`,
            // fifth div
            'end_input_id': `experience-end-date-${NO_OF_EXPERIENCE}`,
            'checkbox_input_id': `experience-check-box-${NO_OF_EXPERIENCE}`,
            'checkbox_label': 'Still working here',
            // sixth div
            'summary_label': 'Summary',
            'summary_input_id': `experience-summary-${NO_OF_EXPERIENCE}`,
            // section id
            'section_id': 'experience-section',
        }
    }


    return data_object
}
/*-----------------------
END HELPER FUNCTIONS
-------------------------*/


/*-----------------------
EVENT HANDLER FUNCTIONS
-------------------------*/

const removeProject = (event) => {
    console.log(event)
    if (event.composedPath()[3].id == 'project-section'){
        NO_OF_PROJECT = NO_OF_PROJECT - 1
    }
    else if (event.composedPath()[3].id == 'education-section'){
        NO_OF_EDUCATION = NO_OF_EDUCATION - 1
    }
    else if (event.composedPath()[3].id == 'experience-section'){
        NO_OF_EXPERIENCE = NO_OF_EXPERIENCE - 1
    }
    document.getElementById(event.composedPath()[3].id).removeChild(event.composedPath()[2])
    // if ()

}
const addTechnicalInput = (event) => {
    const prof_inputs = document.querySelectorAll(`#${event.composedPath()[2].id} .input-group input`)
    let add = true
    let class_ = ''
    let placeholder = prof_inputs[0].placeholder
    let aria_label = prof_inputs[0].ariaLabel
    prof_inputs.forEach((item) => {

        if (item.value == '') {
            add = false
            item.classList.add('is-invalid')
        }
        else {
            item.classList.remove('is-invalid')
        }
    })

    if (prof_inputs[0].classList.contains('title-input')) {
        class_ = 'title-input'
    }
    else {
        class_ = 'skill-input'
    }


    if (add) {
        let new_div = elementCreation('div', ['input-group', 'mt-3'])

        let input_title = elementCreation('input', ['form-control', class_], {
            'type': 'text', 'placeholder': placeholder,
            'aria-label': aria_label, 'aria-describedby': 'button-addon2'
        })


        let remove_btn = elementCreation('button', ['btn', 'btn-outline-danger'], { 'type': 'button' }, inner_text = 'Remove')


        remove_btn.addEventListener('click', removeTechnicalInput)

        new_div.append(input_title, remove_btn)

        // new_div.appendChild(add_btn)
        const input_div = document.getElementById(`${event.composedPath()[2].id}`)


        input_div.appendChild(new_div)

    }

}

const removeTechnicalInput = (event) => {
    const input_div = document.getElementById(`${event.composedPath()[2].id}`)
    input_div.removeChild(event.composedPath()[1])
}

const disableEndDate = (event) => {
    let currInputEndDate = event.composedPath()[1].childNodes[3]
    if (event.srcElement.checked) {
        currInputEndDate.disabled = true
    }
    else {
        currInputEndDate.disabled = false
    }
}

function addSection(event) {
    console.log(event.srcElement.id)
    const data = formCreationHelper(event.srcElement.id)
    let main_div_container = elementCreation('div', ['container', 'row', 'row-cols-md-2', 'row-cols-1', 'gx-md-5', 'gy-md-3', 'mt-3', 'border-top'])

    // HEADING div
    let heading_div = elementCreation('div', ['d-flex', 'mb-3', 'col-md-12', 'align-items-center', 'justify-content-end', 'pt-4'])
    let project_heading = elementCreation('h2', ["fs-3"], {}, inner_text = 'Project-II')
    let project_close_btn = elementCreation('div', ['btn', 'btn-danger', data['close_class']], {}, '', inner_html = 'Delete')

    project_close_btn.addEventListener('click', removeProject)
    heading_div.append(project_close_btn)

    // TITLE div row-1 col-1
    let project_title_div = elementCreation('div', ["col", "mb-3"])
    let project_title_label = elementCreation('label', ["form-label"], { 'for': data['title_input_id'] }, data['title_label'])
    let project_title_input = elementCreation('input', ["form-control", "R1C1"], { 'type': 'text', 'id': data['title_input_id'] })

    project_title_div.append(project_title_label, project_title_input)

    // TECH div row-1 col-2
    let project_tech_div = elementCreation('div', ["col", "mb-3"])
    let project_tech_label = elementCreation('label', ["form-label"], { 'for': data['tech_input_id'] }, data['tech_label'])
    let project_tech_input = elementCreation('input', ["form-control", 'R1C2'], { 'type': 'text', 'id': data['tech_input_id'] })

    project_tech_div.append(project_tech_label, project_tech_input)

    // LIVE DEMO div R-2 C-1
    let project_live_demo_div = elementCreation('div', ["col", "mb-3"])
    let project_live_demo_label = elementCreation('label', ["form-label"], { 'for': data['live_demo_input_id'] }, data['live_demo_label'])
    let project_live_demo_input = elementCreation('input', ["form-control", 'R2C1'], { 'type': 'text', 'id': data['live_demo_input_id'] })

    project_live_demo_div.append(project_live_demo_label, project_live_demo_input)

    // SOURCE div R-2 C-2
    let project_source_div = elementCreation('div', ["col", "mb-3"])
    let project_source_label = elementCreation('label', ["form-label"], { 'for': data['source_input_id'] }, data['source_label'])
    let project_source_input = elementCreation('input', ["form-control", "R2C2"], { 'type': 'text', 'id': data['source_input_id'] })

    project_source_div.append(project_source_label, project_source_input)

    // START DATE div R-3 C-1
    let project_start_date_div = elementCreation('div', ["col", "mb-3"])
    let project_start_date_label = elementCreation('label', ["form-label"], { 'for': data['start_input_id'] }, 'Start Date')
    let project_start_date_input = elementCreation('input', ["form-control", 'R3C1'], { 'type': 'date', 'id': data['start_input_id'] })

    project_start_date_div.append(project_start_date_label, project_start_date_input)

    // END DATE div R-3 C-2
    let project_end_date_div = elementCreation('div', ["col", "mb-3"])
    let project_end_date_label = elementCreation('label', ["form-label"], { 'for': data['end_input_id'] }, 'End Date')
    let project_end_date_input = elementCreation('input', ["form-control"], { 'type': 'date', 'id': data['end_input_id'] })
    let project_check_box_input = elementCreation('input', ["form-check-input", 'diable-date', 'mt-2', 'R3C2'], { 'type': 'checkbox', 'id': data['checkbox_input_id'], 'value': '' })
    let project_check_box_label = elementCreation('label', ["form-check-label", 'mt-1', 'R3C2'], { 'for': data['checkbox_input_id'] }, data['checkbox_label'])
    
    project_check_box_input.addEventListener('click', disableEndDate)
    project_end_date_div.append(project_end_date_label, project_end_date_input, project_check_box_input, project_check_box_label)

    // SUMMARY div R-4 C-1
    let project_summary_div = elementCreation('div', ["col-md-12", "mb-3"])
    let project_summary_label = elementCreation('label', ["form-label"], { 'for': data['summary_input_id'] }, data['summary_label'])
    let project_summary_input = elementCreation('textarea', ["form-control", 'R4C1'], { 'rows': '5', 'id': data['summary_input_id'] })

    project_summary_div.append(project_summary_label, project_summary_input)


    main_div_container.append(heading_div,
        project_title_div,
        project_tech_div,
        project_live_demo_div,
        project_source_div,
        project_start_date_div,
        project_end_date_div,
        project_summary_div
    )
    console.log(data)
    document.getElementById(data['section_id']).appendChild(main_div_container)

}

const saveData = (event) => {
    const id_of_section = event.srcElement.id.split("-")[0]
    const inputs_of_curr_section = document.querySelectorAll(`#${id_of_section} input`)
    inputs_of_curr_section.forEach((item) => {
        if (item.value != '' && item.type != 'file') {
            localStorage.setItem(`${item.id}`, `${item.value}`)
        }
    })
}

const clearData = (event) => {
    const id_of_section = event.srcElement.id.split("-")[0]
    const inputs_of_curr_section = document.querySelectorAll(`#${id_of_section} input`)
    inputs_of_curr_section.forEach((item) => {
        localStorage.removeItem(`${item.id}`)
        item.value = ''
    })
}

/*-----------------------
END EVENT HANDLER FUNCTIONS
-------------------------*/


/*-----------------------
EVENT LISTENERS FUNCTIONS
-------------------------*/

const title_add_btn = document.querySelector('#prof-titles .btn-outline-success')
const skill_add_btn = document.querySelector('#prof-skills .btn-outline-success')

title_add_btn.addEventListener('click', addTechnicalInput)
skill_add_btn.addEventListener('click', addTechnicalInput)


const add_section_btn = document.querySelectorAll('.add-section')

add_section_btn.forEach((item) => {
    item.addEventListener('click', (event) => {
        let section_inputs = document.querySelectorAll(`#${event.composedPath()[3].id} .container input, select`)
        let add_section = true

        section_inputs.forEach((item) => {
            if ((item.localName == 'input' && item.value == '' && (item.type == 'text' || item.type == 'date'))) {
                add_section = false

                item.classList.add('is-invalid')
            } else {
                item.classList.remove('is-invalid')
            }

        })

        if (add_section) {
            addSection(event)
        }
    })
})



const check_box = document.querySelectorAll('.disable-date')
check_box.forEach((item) => {
    item.addEventListener('click', disableEndDate)
})

const save_btns = document.querySelectorAll('.save-btn')
const clear_btns = document.querySelectorAll('.clear-btn')


save_btns.forEach((item) => {
    item.addEventListener('click', saveData)
})
clear_btns.forEach((item) => {
    item.addEventListener('click', clearData)
})

/*-----------------------
END EVENT LISTENER FUNCTIONS
-------------------------*/

window.onload = executeFunctions()
