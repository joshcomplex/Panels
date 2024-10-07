# Panels for Reflex Project
> A Reflex template for even more rapid page development, created for the purpose of allowing Agentic management of content and design.

## Example Usage Hero Section
Three different hero sections types that render the content you need how you need it, without having to dive into the code.

```python
        rx.color_mode.button(position="top-right"),
        hero(type="video", source="https://www.youtube.com/embed/dQw4w9WgXcQ"),
        hero(type="image", source="https://placehold.co/600x400"),
        hero(type="form", source=registration_form(beta_signup())),
```
![Hero Section](<./assets/hero_types.png>)


## Setting Up Your Python Virtual Environment
This guide will help you set up a Python virtual environment for your project that uses Reflex, follows the documentation for: 
- **Large Projects:** https://reflex.dev/blog/2024-03-27-structuring-a-large-app/  
- **Styling:** https://reflex.dev/docs/guide/styling 
- **Forms:** https://reflex.dev/docs/guide/forms

# Setting Up Your Python Virtual Environment

## Step 1: Create a Virtual Environment

Run the following command to create a virtual environment named `venv`:

```bash
python3 -m venv venv
```

## Step 2: Activate the Virtual Environment

### For macOS/Linux:
To activate the virtual environment, use the following command:

```bash
source venv/bin/activate
```

### For Windows:
To activate the virtual environment, use the following command:

```bash
venv\Scripts\activate
```

## Step 3: Install Required Packages

Once the virtual environment is activated, install the required packages using:

```bash
pip install -r requirements.txt
```

## Step 4: Clone the Project Repository

Clone the project repository from GitHub:

```bash
git clone https://github.com/joshcomplex/reflex-panels
```

## Step 5: Initialize Reflex

Finally, initialize Reflex with the following command:

```bash
reflex init
```

# Panels Template Sections
### Current Status Table
| Section Type          | Status       |
|-----------------------|--------------|
| Hero Section          | Draft completed |
| Showcase/Features     | Not Started  |
| Pricing               | Not Started  |
| Call-to-Action (CTA)  | Not Started  |
| Forms                 | In Progress  |

## 1. Hero Section 
- **Importance**: Captures visitors' attention and conveys the core message.
- **Python Name**: `hero()`

## 2. Showcase/Features Section
- **Importance**: Highlights key features or services.
- **Python Name**: `showcase()`

## 3. Pricing Section
- **Importance**: Builds the basic pricing structure for your product or service.
- **Python Name**: `pricing()`

## 4. Call-to-Action (CTA) Section
- **Importance**: Encourages user interaction or conversion.
- **Python Name**: `cta()`

## 5. Pre Built Forms
- **Importance**: Provides contact information or a form for inquiries.
- **Python Name**: `registration_form(form_name)`



## Additional Notes

- Make sure to activate the virtual environment each time you start a new terminal session for this project.
- To deactivate the virtual environment when you're done, simply run:

```bash
deactivate
```