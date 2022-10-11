def jsFileData(data):
    return f'''
/* -----------------------------
DATAS
-------------------------------- */

let personal_data = {data['personal_data']}
let links_data = {data['link_data']}
let prof_skill_data = {data['prof_skill_data']}
let project_data = {data['project_data']}
let education_data = {data['education_data']}
let experience_data = {data['experience_data']}

/* -----------------------------
END DATAS
-------------------------------- */

/* -----------------------------
HELPER FUNCTIONS
-------------------------------- */

function setAttributes(el, options) {{
  Object.keys(options).forEach(function (attr) {{
      el.setAttribute(attr, options[attr]);
  }})
}}

const elementCreation = (element, classes = [], attributes = {{}}, inner_text = '', inner_html = '') => {{
  let new_element = document.createElement(element)
  new_element.classList.add(...classes)
  setAttributes(new_element, attributes)
  new_element.innerText = inner_text
  if (inner_html !== '') {{
      new_element.innerHTML = inner_html
  }}
  return new_element
}}

const elementCreationNS = (element_data, classes=[], attributes = {{}}, inner_text = '', inner_html = '') => {{
  let new_element = document.createElementNS(element_data[0], element_data[1])
  new_element.classList.add(...classes)
  setAttributes(new_element, attributes)
  new_element.innerText = inner_text
  if (inner_html !== '') {{
    new_element.innerHTML = inner_html
  }}
  return new_element
}}


/* -----------------------------
END HELPER FUNCTIONS
-------------------------------- */

/* -----------------------------
SVG CREATORS FUNCTIONS
-------------------------------- */

const svgCheckCreator = () => {{
  let svg = elementCreationNS(['http://www.w3.org/2000/svg','svg'], ['icon'], {{ 'style': "width:24px;height:24px", 'viewBox':  "0 0 24 24", 'stroke-width': "1.5", 'stroke': "#00b341", 'fill':"none", 'stroke-linecap':"round", 'stroke-linejoin':"round"}})
  let path_1 = elementCreationNS(['http://www.w3.org/2000/svg', 'path'], [], {{'stroke': 'none', 'd': "M0 0h24v24H0z", "fill":"none"}})
  let circle_1 = elementCreationNS(['http://www.w3.org/2000/svg', 'circle'], [], {{'cx':"12", "cy":"12", "r":"9"}})
  let path_2 = elementCreationNS(['http://www.w3.org/2000/svg', 'path'], [], {{'d': "M9 12l2 2l4 -4"}})
  svg.append(path_1, circle_1, path_2)
  return svg

}}

const svgAlertDateCreator = (info) => {{
  let path_img = ''
  if (info){{
    path_img = "M11,9H13V7H11M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M11,17H13V11H11V17Z"

  }} else {{
    path_img = "M19,19H5V8H19M16,1V3H8V1H6V3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3H18V1M17,12H12V17H17V12Z"
  }}
  let svg_info = elementCreationNS(['http://www.w3.org/2000/svg','svg'], ['icon'], {{ 'style': "width:24px;height:24px", 'viewBox':  "0 0 24 24"}})
  let path_info = elementCreationNS(['http://www.w3.org/2000/svg', 'path'], [], {{ 'fill': 'currentColor', 'd': path_img }})
  svg_info.appendChild(path_info)

  return svg_info
}}

/* -----------------------------
SVG CREATORS FUNCTIONS
-------------------------------- */
/* -----------------------------
CARD CREATOR FUNCTIONS
-------------------------------- */
// let image_url = 'https://images.unsplash.com/photo-1578944032637-f09897c5233d?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ'
let image_url = './img/project-img.jpg'

const addProjectCard = (data) => {{
  const main_ul = document.getElementById('project-container')

  let li = elementCreation('li', ['booking-card'], {{'style': `background-image: url(${{image_url}})`}})
  
  let main_div_1 = elementCreation('div', ['book-container'])
  let btns_div = elementCreation('div', ['content'])
  let live_demo_a = elementCreation('a', [], {{'href': data['live']}}, '', '<button class="btn">Live Demo</button>')
  let source_code_a = elementCreation('a', [], {{'href': data['source']}}, '', '<button class="btn">Source Code</button>')

  btns_div.append(live_demo_a, source_code_a)
  main_div_1.appendChild(btns_div)


  let main_div_2 = elementCreation('div', ['informations-container'])
  let h2_title = elementCreation('h2', ['title'], {{}}, data['title'])
  let p_tech_stack = elementCreation('p', ['sub-title'], {{}}, data['tech'])
  let information_div = elementCreation('div', ['more-information'])
  
  let info_date_div = elementCreation('div', ['info-and-date-container'])
  let info_div = elementCreation('div', ['box', 'info'])
  let svg_info = svgAlertDateCreator(true)
  let p_project_status = elementCreation('p', [], {{}}, data['status'])
  info_div.append(svg_info, p_project_status)

  let date_div = elementCreation('div', ['box', 'date'])
  let svg_date = svgAlertDateCreator(false)
  let p_project_date = elementCreation('p', [], {{}}, data['duration'])
  date_div.append(svg_date, p_project_date)

  
  info_date_div.append(info_div, date_div)

  let project_description = elementCreation('p', ['disclaimer'], {{}}, data['summary'])

  information_div.append(info_date_div, project_description)

  main_div_2.append(h2_title, p_tech_stack, information_div)

  li.append(main_div_1, main_div_2)
  main_ul.appendChild(li)

}}


const addEducationCard = (id, school, date, subject, location, description) => {{
  const resume_section = document.getElementById(id)

  let div = elementCreation('div', ['resume-item'])
  let h4_college = elementCreation('h4', [], {{}}, school)
  let h5_date = elementCreation('h5', [], {{}}, `${{date}}`)
  let p_subject = elementCreation('p', [], {{}}, '', `<em>${{subject}}</em>`)
  let p_location = elementCreation('p', [], {{}}, '', `<em>${{location}}</em>`)
  let p_desc = elementCreation('p', [], {{}}, `${{description}}`)

  div.append(h4_college, h5_date, p_subject, p_location, p_desc)
  resume_section.appendChild(div)
}}


const addExperienceCard = (id, role, company, date, location, description) => {{
  const resume_section = document.getElementById(id)

  let div = elementCreation('div', ['resume-item'])
  let h4_role = elementCreation('h4', [], {{}}, `${{role}} - ${{company}}`)
  let h5_date = elementCreation('h5', [], {{}}, `${{date}}`)
  let p_location = elementCreation('p', [], {{}}, '', `<em>${{location}}</em>`)
  let p_desc = elementCreation('p', [], {{}}, `${{description}}`)

  div.append(h4_role, h5_date, p_location, p_desc)
  resume_section.appendChild(div)
}}

/* -----------------------------
END CARD CREATOR FUNCTIONS
-------------------------------- */

/* -----------------------------
DATA SETTERS
-------------------------------- */
const name_set = document.querySelectorAll('.set-name')
name_set.forEach((item) => {{
  item.innerText = `${{personal_data['first_name']}} ${{personal_data['last_name']}}`
}})

const about_text = document.getElementById('about-text')
about_text.innerText = `${{personal_data['about']}}`

const link_ids = ['git', 'linkedin', 'facebook', 'instagram', 'twitter']
for (let link_id of link_ids) {{
  let links = document.querySelectorAll(`${{link_id}}-link`)
  links.forEach((link) => {{
    link.href = links_data[link_id]
  }})
}}

const resume_link = document.getElementById('resume-link')
resume_link.href = links_data['resume']

const address = document.getElementById('address')
const phone = document.getElementById('phone')
const mail = document.getElementById('mail')

address.innerText = `${{personal_data['address']}} ${{personal_data['address2']}} ${{personal_data['city']}} ${{personal_data['state']}} ${{personal_data['zip']}}`
phone.innerText = personal_data['phone']
mail.innerText = personal_data['email']

// projects

for (let project in project_data) {{
  let data = {{}}
  data['live'] = project_data[project]['project-live-link']
  data['source'] = project_data[project]['project-source-code']
  data['title'] = project_data[project]['project-title']
  data['tech'] = project_data[project]['project-tech']
  data['check'] = project_data[project]['project-check-box']
  data['summary'] = project_data[project]['project-summary']

  if (data['check']){{
    end = 'present'
  }}
  else if(project_data[project]['project-end-date'] != ''){{
    end = project_data[project]['project-end-date'].slice(0, 7)
  }}
  data['duration'] = `${{project_data[project]['project-start-date'].slice(0, 4)}} - ${{end}}`
  addProjectCard(data)
}}

// EDUCATION
for (let education in education_data) {{

  let id = 'education-items'
  location_ = education_data[education]['education-location']
  school = education_data[education]['education-school']
  subject = education_data[education]['education-subject']
  check = education_data[education]['education-check-box']
  summary = education_data[education]['education-summary']
  let end = ''
  if (check){{
    end = 'present'
  }}
  else if(education_data[education]['education-end-date'] != ''){{
    end = education_data[education]['education-end-date'].slice(0, 7)
  }}
  duration = `${{education_data[education]['education-start-date'].slice(0, 4)}} - ${{end}}`
  addEducationCard(id, school, duration, subject, location_, summary)
}}

// EXPERIENCE
for (let experience in experience_data) {{

  let id = 'experience-items'
  location_ = experience_data[experience]['experience-location']
  role = experience_data[experience]['experience-role']
  company = experience_data[experience]['experience-company']
  check = experience_data[experience]['experience-check-box']
  summary = experience_data[experience]['experience-summary']
  let end = ''
  if (check){{
    end = 'present'
  }}
  else if(experience_data[experience]['experience-end-date'] != ''){{
    end = experience_data[experience]['experience-end-date'].slice(0, 7)
  }}
  duration = `${{experience_data[experience]['experience-start-date'].slice(0, 4)}} - ${{end}}`
  addExperienceCard(id, role, company, duration, location_, summary)
}}
/* -----------------------------
END DATA SETTERS
-------------------------------- */

// typing effect code snippet
let isReady = true
let t = 300

const jobs = prof_skill_data['title_data']
let job_count = 0
let job_index = 0

let currentJobText = ''
let jobLetter = '';

(function type() {{
  if (job_count === jobs.length) {{
    job_count = 0
  }}
  if (!isReady) {{
    t = 50
    currentJobText = jobs[job_count]
    letter = currentJobText.slice(0, ++job_index)
    // document.querySelector('.typing').textContent = letter
    document.querySelector('.typing').innerHTML = `<span style="color: #1a2e39;">I'm a </span>${{letter}}`

    if (letter.length === currentJobText.length) {{

      isReady = true
    }}
  }}

  if (isReady) {{
    t = 50
    currentJobText = jobs[job_count]
    if (job_index === currentJobText.length) {{
      t = 2000
    }}
    letter = currentJobText.slice(0, job_index)
    job_index -= 1
    document.querySelector('.typing').innerHTML = `<span style="color: #1a2e39;">I'm a </span>${{letter}}`
    if (letter.length === 0) {{
      isReady = false
      t = 100
      job_count++
      job_index = 0
    }}

  }}
  setTimeout(type, t)
}}())


// Tab menu toggle in small devices
const ham_menu = document.getElementById('ham-btn')
const section = document.querySelectorAll('section')
const nav = document.getElementById('navbar')

const toggleTab = () => {{
  nav.classList.toggle('active')
  ham_menu.classList.toggle('fa-xmark')
  ham_menu.classList.toggle('fa-bars')
  ham_menu.classList.toggle('active')

  section.forEach((item) => {{
    item.classList.toggle('tab-active')
  }})
}}

ham_menu.addEventListener('click', toggleTab)

section.forEach((item) => {{
  item.addEventListener('click', () => {{
    if (nav.classList.contains('active')) {{
      toggleTab()
    }}
  }})
}})



// creating skills html from js
let skill_container = document.getElementById('skills')
let skills = prof_skill_data['skill_data']


for (let skill of skills) {{
  let skill_card = document.createElement('li')
  skill_card.className = 'skill-card'
  let skill_heading = document.createElement('h2')
  skill_heading.innerText = skill
  skill_card.appendChild(skill_heading)
  skill_container.appendChild(skill_card)
}}





// navbar color change on scroll

const select = (el, all = false) => {{ // DOM selection helper function 
  el = el.trim()
  if (all) {{
    return [...document.querySelectorAll(el)]
  }} else {{
    return document.querySelector(el)
  }}
}}

let navbarlinks = select('#navbar .scrollto', true)
const navbarlinksActive = () => {{
  let position = window.scrollY + 200
  navbarlinks.forEach(navbarlink => {{
    if (!navbarlink.hash) return
    let section = select(navbarlink.hash)
    if (!section) return
    if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {{
      navbarlink.classList.add('active')
    }} else {{
      navbarlink.classList.remove('active')
    }}
  }})
}}
window.addEventListener('load', navbarlinksActive)
window.addEventListener('scroll', navbarlinksActive)




// Reveal element effect on scroll
window.addEventListener('scroll', reavealElements)

function reavealElements() {{


  let reveals = document.querySelectorAll('.reveal')

  for (let i = 0; i < reveals.length; i++) {{
    let windowHeight = window.innerHeight;
    let revealTop = reveals[i].getBoundingClientRect().top
    let revealPoint = 150

    if (revealTop < windowHeight - revealPoint) {{
      reveals[i].classList.add('active')
    }}
  }}
}}




    '''