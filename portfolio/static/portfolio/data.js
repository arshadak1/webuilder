const form = document.getElementById('form')
const prof_skill_inp = document.getElementById('prof-skill-data')
const project_data_inp = document.getElementById('project-data')
const education_data_inp = document.getElementById('education-data')
const experience_data_inp = document.getElementById('experience-data')



/*-----------------------
HELPER FUNCTIONS
-------------------------*/

const getTechnicalData = () => {
    let prof_skill_data = {}
    const titles = document.querySelectorAll('#technical .title-input')
    const skills = document.querySelectorAll('#technical .skill-input')
    let title_data = []
    let skill_data = []
    titles.forEach((title) => {
        if (title.value != '') {
            title_data.push(title.value)
        }
    })

    skills.forEach((skill) => {
        if (skill.value != '') {
            skill_data.push(skill.value)
        }
    })
    prof_skill_data['title_data'] = title_data
    prof_skill_data['skill_data'] = skill_data
    
    return prof_skill_data
}

const getSectionData = (section) => {
    let data = {}
    const project_section_container = document.querySelectorAll(`#${section}-section .container`)
    project_section_container.forEach((container, index) => {
        let curr_container_data = {}
        for (let i = 0; i < container.children.length; i++) {
            let curr_child = container.children[i]

            for (let j = 0; j < curr_child.children.length; j++) {

                let node_name = curr_child.children[j].localName

                if (node_name == 'input' || node_name == 'textarea') {
                    curr_container_data[`${curr_child.children[j].id.slice(0, -2)}`] = curr_child.children[j].value

                }
            }
        }
        data[`${section}-${index}`] = curr_container_data


    })
    console.log(data)
    return data

}

/*-----------------------
END HELPER FUNCTIONS
-------------------------*/

/*-----------------------
HANDLER FUNCTIONS
-------------------------*/

const formSubmitHandler = (event) => {

    let prof_skill_data = getTechnicalData()
    prof_skill_inp.value = JSON.stringify(prof_skill_data)

    let project_data = getSectionData('project')
    let education_data = getSectionData('education')
    let experience_data = getSectionData('experience')

    project_data_inp.value = JSON.stringify(project_data)
    education_data_inp.value = JSON.stringify(education_data)
    experience_data_inp.value = JSON.stringify(experience_data)

}

/*-----------------------
END HANDLER FUNCTIONS
-------------------------*/

/*-----------------------
EVENT LISTENERS
-------------------------*/

form.addEventListener('submit', formSubmitHandler)

/*-----------------------
END EVENT LISTENERS
-------------------------*/
