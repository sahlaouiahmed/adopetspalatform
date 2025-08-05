# Adopets Platform

Welcome to Adopets Platform, your go-to solution for pet adoption! Our platform is designed to simplify and enhance the pet adoption process, making it easier for potential adopters to connect with pet owners. With Adopets, finding a loving home for every pet is just a few clicks away. Whether you're looking to adopt a pet or rehome a pet, our user-friendly interface and powerful search capabilities ensure a seamless experience for all users.

Additionally, explore our comprehensive library of pet care articles to provide the best for your new furry friends. Share your experiences, tips, and stories with other pet lovers in our community, and learn from others' experiences to make the journey of pet adoption even more rewarding.

Our website is deployed on Heroku. Check it out [here](https://adopetsplatform-4e35c86a8c8e.herokuapp.com/).


## User Stories

User stories are part of the Agile framework for software development. They guide the selection of features built on this website and explain the reasoning behind the chosen features.

### Adoption Stories

#### As a Visitor
1. I want to view the homepage.
   - **Acceptance Criteria**:
     - Displays a welcoming message
     - Lists pets available for adoption
     - Allows navigation to different sections

#### As a User
2. I want to filter pets by species, breed, city, country, and posted_by.
   - **Acceptance Criteria**:
     - Filter form available on the pet listings page
     - Filters applied display matching pets
3. I want to create an account.
   - **Acceptance Criteria**:
     - Sign-up form collects necessary details
     - Confirmation email after successful sign-up
4. I want to log in to my account.
   - **Acceptance Criteria**:
     - Login form for returning users
     - Successful login redirects to the homepage or profile page
5. I want to add a new pet for adoption.
   - **Acceptance Criteria**:
     - Form to add new pet details (name, species, breed, age, gender, description, city, country, and photo)
     - Success message after adding a pet
     - New pet appears in the list of pets available for adoption
6. I want to view the details of a pet.
   - **Acceptance Criteria**:
     - Clicking on a pet listing displays detailed information
     - Details page includes the pet's name, species, breed, age, gender, description, city, country, and photo
7. I want to edit a pet I posted.
   - **Acceptance Criteria**:
     - Access an edit form for posted pets
     - Update the pet's details and save changes
     - Success message after updating the pet
8. I want to delete a pet I posted.
   - **Acceptance Criteria**:
     - Delete posted pets
     - Confirmation prompt before deleting
     - Success message after deletion
     - The pet is removed from the listings
9. I want to adopt a pet.
   - **Acceptance Criteria**:
     - Form to submit an adoption request for a pet
     - Success message after submitting the request
     - The request appears in the user's adoption requests list
10. I want to view, delete, and edit my pet adoption requests.
    - **Acceptance Criteria**:
      - List page displays the user's adoption requests
      - Each request includes options to view details, edit, or delete
      - Success messages after updating or deleting a request
11. I want to view my received adoption requests.
    - **Acceptance Criteria**:
      - List page displays adoption requests received for the user's posted pets
      - Each request includes options to view details and update status
12. I want to change the status of a received adoption request.
    - **Acceptance Criteria**:
      - Form to update the status of a received adoption request (e.g., approved, denied)
      - Success message after updating the status
      - The updated status appears in the received requests list

### Article Stories

#### As a Visitor
1. I want to read pet care articles.
   - **Acceptance Criteria**:
     - Article list page displaying various pet care articles
     - Filter articles by categories like Dogs, Cats, Fish, Birds
     - Clicking on an article shows the full content

#### As a User
1. I want to read pet care articles.
   - **Acceptance Criteria**:
     - Article list page displaying various pet care articles
     - Filter articles by categories like Dogs, Cats, Fish, Birds
     - Clicking on an article shows the full content
2. I want to add a new pet care article.
   - **Acceptance Criteria**:
     - Form to add new article details (title, content, category)
     - Success message after adding an article
     - New article appears in the list of pet care articles
3. I want to delete an article I posted.
   - **Acceptance Criteria**:
     - Delete posted articles
     - Confirmation prompt before deleting
     - Success message after deletion
     - The article is removed from the listings
4. I want to view a list of articles I posted.
   - **Acceptance Criteria**:
     - List page displays articles posted by the user
     - Each article includes a link to edit or delete it
5. I want to edit an article I posted.
   - **Acceptance Criteria**:
     - Access an edit form for posted articles
     - Update the article's details and save changes
     - Success message after updating the article

*These user stories were created by referring to this [documentation](https://www.nimblework.com/agile/user-stories/).*



## Key Features

### Posting Pets
Easily post pets available for adoption on our platform. Provide detailed information, including photos, breed, age, and any special requirements. This helps potential adopters find the perfect match quickly and efficiently.

### Adoption Requests
Manage adoption requests seamlessly. Potential adopters can express their interest in adopting pets, and pet owners or shelters can review and respond to these requests. Our streamlined process ensures a smooth and transparent adoption experience for everyone involved.

### Research Using Filters
Find the ideal pet using our powerful search filters. Filter by species, breed, age, location, and more to narrow down your options and find pets that match your preferences. Our intuitive search functionality makes it easy to discover pets that are looking for a loving home.

### Account Creation
Sign up and create an account to start using the Adopets Platform. Whether you're a pet owner looking to rehome a pet or a potential adopter searching for a new companion, having an account allows you to manage your listings, adoption requests, and communication with ease.

### Articles of Pet Care
Explore our comprehensive library of articles on pet care. From feeding tips to grooming guides, our articles are designed to help pet owners provide the best care for their furry friends. Stay informed and ensure your pets are happy and healthy with our expert advice.

## Technologies Used

### Django
Django is the backbone of our platform. It’s a high-level Python web framework that encourages rapid development and clean, pragmatic design. Django takes care of much of the hassle of web development, allowing us to focus on writing your app without needing to reinvent the wheel. 

### Mysql
We use Mysql as our database management system. It’s a powerful, open-source object-relational database system that has earned a strong reputation for reliability, feature robustness, and performance.

### JavaScript
JavaScript powers the interactive elements of our site, ensuring a smooth and dynamic user experience. It's an essential technology for making our web pages more engaging and functional.

### HTML
HTML (HyperText Markup Language) is used to structure our web pages and content. It forms the skeleton of our web application, providing the essential building blocks for layout and organization.

### CSS
CSS (Cascading Style Sheets) is used for styling our HTML. It allows us to create a visually appealing interface that is both user-friendly and consistent across different browsers and devices.

### Bootstrap
Bootstrap is a popular front-end framework for developing responsive and mobile-first websites. It provides a collection of CSS and JavaScript components that make it easier to design beautiful and responsive web pages quickly.


## Website Functionalities

### User Registration and Login
- **Create an Account**: Users can sign up and create an account by providing their username, email, and password. This allows them to access additional features and manage their activity on the platform.
- **Login**: Registered users can log in to their accounts using their credentials, ensuring secure access to their personalized dashboard.

![User sign up and login interface](static/images/readme_photos/sign_up&login.png)

### Dashboard
- **User Dashboard**: Once logged in, users have access to a personalized dashboard where they can manage their posted pets, adoption requests, recieved adoption requests and their posted articles . The dashboard provides an overview of their activity on the platform.

![Home page ](static/images/readme_photos/home.png)


### Posting Pets
- **Add New Pet**: Users can post pets available for adoption by providing detailed information such as name, species, breed, age, gender, description, and photos. This helps potential adopters find the right pet easily.
- **Manage Posts**: Users can edit or delete their posted pets from their dashboard, ensuring that the information is always up-to-date.

![Postingpets](static/images/readme_photos/My-Posted-Pets.png)


### Adoption Requests
- **Submit Adoption Request**: Potential adopters can express their interest in adopting a pet by submitting an adoption request. They can write a message to the pet owner explaining why they are a good fit for the pet.
- **View Adoption Requests**: Pet owners can view the adoption requests they have received, including messages from potential adopters. This allows them to review and respond to requests directly from their dashboard.

![AdoptionRequests](static/images/readme_photos/AdoptionRequests.png)

### Pet Care Articles
- **Browse Articles**: Users can explore a comprehensive library of pet care articles covering various topics such as feeding, grooming, training, and health. The articles are designed to provide valuable information to pet owners and adopters.
- **Write and Share Articles**: Registered users can contribute to the community by writing and sharing their own articles. This allows them to share their experiences and tips with other pet lovers.

![AdoptionRequests](static/images/readme_photos/Petcaretips.png)

### Search and Filters
- **Search for Pets**: Users can search for pets based on various criteria such as species, breed, age, and location. This helps them find pets that match their preferences quickly and easily.
- **Filter Results**: Users can apply filters to narrow down their search results, making it easier to find the perfect pet.

![research filters](static/images/readme_photos/filters.png)



## Entity-Relationship Diagrams (ERD)

Here are the ERDs for each model in the Adopets Platform database.

### User Model

#### Diagram:

Here's the Entity-Relationship Diagram (ERD) for the Django standard User model:

![User Model ERD](static/images/readme_photos/user_model.png)

#### Relationships:

- Groups: A many-to-many relationship with the Group model.

- Permissions: A many-to-many relationship with the Permission model.

### Pet Model 

#### Diagram:

![Pet Model ERD](static/images/readme_photos/pet_model.png)

#### Relationships
- User has a one-to-many relationship with Pet (a single user can post multiple pets).

### AdoptionRequest Model

#### Diagram:

![ AdoptionRequest Model ERD](static/images/readme_photos/AdoptionRequest_Model.png)

#### Relationships

- User has a one-to-many relationship with AdoptionRequest (a single user can make multiple adoption requests).

- Pet has a one-to-many relationship with AdoptionRequest (a single pet can have multiple adoption requests).

### Article Model

#### Diagram:

![ Article Model ERD](static/images/readme_photos/Article_Model.png)

#### Relationships

- User has a one-to-many relationship with Article (a single user can author multiple articles).



## Automated Unit Tests

To ensure the robustness and reliability of the Adopets Platform, we created comprehensive tests for all forms using Django's `TestCase` framework. Here are the details of the tests we implemented:

### Form Tests

#### User Registration Form
We tested the `UserRegistrationForm` to ensure that users can successfully register with valid data, and that errors are properly handled when the data is invalid or incomplete.

#### Pet Form
We thoroughly tested the `PetForm` to confirm that users can add new pets with complete and valid information, including an image upload. We also verified that the form correctly handles missing or invalid data.

#### Adoption Request Form
The `AdoptionRequestForm` was tested to check that adoption requests can be submitted with a pre-filled message, and that the form is valid with both the default and custom initial messages.

#### Pet Search Form
We tested the `PetSearchForm` to ensure that users can search for pets based on various criteria such as species, breed, city, country, and posted by. The form was validated to work correctly with full, partial, and blank data.

#### Adoption Request Filter Form
We tested the `AdoptionRequestFilterForm` to confirm that users can filter adoption requests based on their status (pending, approved, rejected). The form was tested with valid, empty, and invalid data to ensure proper functionality.

### Views Tests

#### IndexViewTests
- **setUp**: Initializes the test client, creates a user, logs in the user, creates 15 pet instances, and sets the URL for the index view.
- **test_index_view_status_code**: Tests that the view returns a status code of 200 and uses the correct template.
- **test_index_view_filters**:Tests the filter functionality to ensure pets can be filtered by species, breed, city, country, and posted_by.
![IndexViewTests](static/images/readme_photos/indexView.png)

#### PetDetailViewTests
- **test_pet_detail_view_status_code**: Ensures the pet detail view returns a status code of 200 and uses the correct template.
- **test_pet_detail_view_content**: Ensures the pet detail view contains the correct pet information.
![PetDetailViewTests](static/images/readme_photos/petDetails.png)

#### AddPetViewTests
- **setUp**: Initializes the test client, creates a user, logs in the user, and sets the URL for the `add_pet` view.
- **test_add_pet_view_get**: Tests that the view responds correctly to a GET request, uses the correct template, and contains the appropriate form.
- **test_add_pet_view_post_valid**: Tests a valid POST request to add a new pet, checks for a redirect to the `index` page, and verifies that the new pet was created.
- **test_add_pet_view_post_invalid**: Tests an invalid POST request (missing required fields), ensures the form is re-rendered with errors, and verifies that no pet is created.
![AddPetViewTests](static/images/readme_photos/addPet.png)

#### MyAdoptionRequestsViewTests
- **test_my_adoption_requests_view_status_code**: Ensures the adoption requests view returns a status code of 200 and uses the correct template.
- **test_my_adoption_requests_view_with_requests**: Ensures the view displays the user's adoption requests.
- **test_my_adoption_requests_view_with_filter**: Ensures the view filters adoption requests by status.
- **test_my_adoption_requests_view_no_requests**: Ensures the view handles the case with no adoption requests.
- **test_login_required**: Ensures the view redirects to the login page if the user is not logged in.
![MyAdoptionRequestsViewTests](static/images/readme_photos/MyadoRequests.png)

#### ReceivedAdoptionRequestsViewTests
- **setUp**: Initializes the test client, creates a user, logs in the user, creates a pet and an adoption request, and sets the URL for the received adoption requests view.
- **test_received_adoption_requests_view_status_code**: Tests that the view returns a status code of 200 and uses the correct template.
- **test_received_adoption_requests_view_with_requests**: Ensures the view displays the received adoption requests and their status.
- **test_login_required**: Ensures the view redirects to the login page if the user is not logged in.
![ReceivedAdoptionRequestsViewTests](static/images/readme_photos/recievedAdoRequests.png)

#### UpdateStatusViewTests
- **setUp**: Initializes the test client, creates a user, logs in the user, creates a pet and an adoption request, and sets the URL for the update status view.
- **test_update_status_view_valid_status**: Tests a valid POST request to update the adoption request status and ensures the status is updated correctly.
- **test_update_status_view_invalid_status**: Tests an invalid POST request (invalid status) and ensures the status remains unchanged.
- **test_update_status_view_login_required**: Ensures the view redirects to the login page if the user is not logged in.
![UpdateStatusViewTests](static/images/readme_photos/updateStatus.png)

#### DeletePetViewTests
- **setUp**: Initializes the test client, creates a user, logs in the user, creates a pet, and sets the URL for the delete pet view.
- **test_delete_pet_view_status_code**: Tests that the view returns a status code of 302, redirects correctly, and ensures the pet is deleted.
- **test_delete_pet_view_message**: Ensures a success message is displayed after the pet is deleted.
- **test_delete_pet_view_login_required**: Ensures the view redirects to the login page if the user is not logged in.
![DeletePetViewTests](static/images/readme_photos/deletePet.png)

#### MyPostedPetsViewTests
- **setUp**: Initializes the test client, creates a user, logs in the user, creates a pet, and sets the URL for the my posted pets view.
- **test_my_posted_pets_view_status_code**: Tests that the view returns a status code of 200 and uses the correct template.
- **test_my_posted_pets_view_with_pets**: Ensures the view displays the user's posted pets.
- **test_my_posted_pets_view_no_pets**: Tests the view when there are no posted pets.
- **test_login_required**: Ensures the view redirects to the login page if the user is not logged in.
![MyPostedPetsViewTests](static/images/readme_photos/postedPets.png)

#### DeleteAdoptionRequestViewTests
- **setUp**: Initializes the test client, creates a user, logs in the user, creates a pet and an adoption request, and sets the URL for the delete adoption request view.
- **test_delete_adoption_request_view_status_code**: Tests that the view returns a status code of 302, redirects correctly, and ensures the adoption request is deleted.
- **test_delete_adoption_request_view_message**: Ensures a success message is displayed after the adoption request is deleted.
- **test_delete_adoption_request_view_login_required**: Ensures the view redirects to the login page if the user is not logged in.
![DeleteAdoptionRequestViewTests](static/images/readme_photos/deleteAdoptionRequest.png)

#### EditPetViewTests
- **setUp**: Initializes the test client, creates a user, logs in the user, creates a pet, and sets the URL for the edit pet view.
- **test_edit_pet_view_status_code**: Tests that the view returns a status code of 200, uses the correct template, and contains the appropriate form.
- **test_edit_pet_view_post_valid**: Tests a valid POST request to update the pet details and ensures the details are updated correctly.
- **test_edit_pet_view_post_invalid**: Tests an invalid POST request (missing required fields) and ensures the form is re-rendered with errors.
- **test_edit_pet_view_permission_denied**: Ensures a user who is not the author of the pet is redirected and cannot edit the pet.
![EditPetViewTests](static/images/readme_photos/editPet.png)

#### ArticleListViewTests
- **setUp**: Initializes the test client, creates a user, logs in the user, creates 5 article instances, and sets the URL for the `article_list` view.
- **test_article_list_view_status_code**: Tests that the view returns a status code of 200 and uses the correct template.
- **test_article_list_view_filters**: Tests the filter functionality to ensure articles can be filtered by category.
- **test_article_list_view_all**: Ensures all articles are listed when no category filter is applied.
- **test_article_list_view_login_required**: Ensures the view is accessible even if the user is not logged in.
![ArticleListViewTests](static/images/readme_photos/articlesList.png)

#### ArticleDetailViewTests
- **test_article_detail_view_status_code**: Ensures the article detail view returns a status code of 200 and uses the correct template.
- **test_article_detail_view_content**: Ensures the article detail view contains the correct article information.
![ArticleDetailViewTests](static/images/readme_photos/articleDetails.png)

#### MyArticlesViewTests
- **test_my_articles_view_status_code**: Ensures the my articles view returns a status code of 200 and uses the correct template.
- **test_my_articles_view_content**: Ensures the view displays the user's articles.
- **test_login_required**: Ensures the view redirects to the login page if the user is not logged in.
![MyArticlesViewTests](static/images/readme_photos/myArticles.png)

#### EditArticleViewTests
- **test_edit_article_view_status_code**: Ensures the edit article view returns a status code of 200 and uses the correct template.
- **test_edit_article_view_post_valid**: Ensures a valid POST request redirects to the my articles page and updates the article.
- **test_edit_article_view_post_invalid**: Ensures an invalid POST request re-renders the form with errors.
- **test_edit_article_view_permission_denied**: Ensures a user who is not the author of the article is redirected.
![EditArticleViewTests](static/images/readme_photos/editArticle.png)

#### DeleteArticleViewTests
- **test_delete_article_view_status_code**: Ensures the delete article view returns a status code of 302 and redirects correctly.
- **test_delete_article_view_message**: Ensures a success message is displayed after the article is deleted.
- **test_delete_article_view_login_required**: Ensures the view redirects to the login page if the user is not logged in.
![DeleteArticleViewTests](static/images/readme_photos/deleteArticle.png)

#### AboutViewTests
- **test_about_view_status_code**: Ensures the about view returns a status code of 200 and uses the correct template.
![AboutViewTests](static/images/readme_photos/about_usView.png)

### Test Files

You can find the test cases for views and forms of adopets_platform app in the tests directory: [Click here to view the files on GitHub](https://github.com/sahlaouiahmed/adopets_platform/tree/main/adopets_platform/tests).

You can find the test cases for views and forms of tips app in the tests directory: [Click here to view the files on GitHub](https://github.com/sahlaouiahmed/adopets_platform/tree/main/tips/tests).

You can find the test cases for views and forms of about_us app in the test.py file : [Click here to view the file on GitHub](https://github.com/sahlaouiahmed/adopets_platform/blob/main/about_us/tests.py).

### Code Validation

The HTML and CSS files of this project were validated using the following tools:
- [W3C Markup Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

These tools helped ensure that the code adheres to web standards and is free of errors.

## Deployment

This project is deployed to Heroku using the GitHub integration. Follow the steps below to deploy a version of this project.

### Steps to Deploy

1. **Create a Heroku App**:
   - Log in to a Heroku account and create a new app by clicking the "New" button on the dashboard and selecting "Create new app." Provide the app a unique name and select the appropriate region.

2. **Connect GitHub Repository**:
   - In the Deploy tab of the newly created app, locate the "Deployment method" section.
   - Select "GitHub" as the deployment method.
   - Connect the GitHub account and select the repository to deploy.

3. **Environment Variables**:
   - Set up environment variables in the "Settings" tab of the Heroku app. Add the following environment variables:
     - `SECRET_KEY`: The Django secret key.
     - `DATABASE_URL`: The database URL.

4. **Procfile**:
   - Ensure a `Procfile` with the following content is present:
     ```
     web: gunicorn CI_project4.wsgi
     ```

5. **Collect Static Files**:
   - Ensure `settings.py` is configured to collect static files. Add the following settings:
     ```python
     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
     STATIC_URL = '/static/'

     # Extra places for collectstatic to find static files.
     STATICFILES_DIRS = (
         os.path.join(BASE_DIR, 'static'),
     )
     ```

6. **Push to GitHub**:
   - Ensure all changes are committed to the GitHub repository.

7. **Deploy via Heroku Dashboard**:
   - In the Deploy tab, scroll down to the "Manual deploy" section.
   - Select the main branch.
   - Click "Deploy Branch."


## Credits

### Tools and Technologies

- **Django**: The high-level Python web framework that enabled rapid development.
- **Mysql**: For robust and scalable database 
- **Bootstrap**: For styling and responsive design.
- **Font Awesome**: For beautiful and scalable icons.
- **Crispy Forms**: For better form styling and control.
- **TestCase**: For writing comprehensive tests to ensure the application works as expected.

### Inspiration

- Inspired by various pet adoption platforms that aim to simplify and enhance the pet adoption process.
- Referenced best practices from several online resources and tutorials to enhance the functionality and design of the project, including:
  - **Django Documentation**: Official documentation for Django, covering everything from installation to advanced features.
  - **Bootstrap Documentation**: Official documentation for Bootstrap, including examples and templates for responsive design.
  - **Stack Overflow**: A community-driven Q&A site where you can find answers to a wide range of programming questions.


## Future Enhancements

We have some exciting plans for the Adopets Platform to make it even more user-friendly and comprehensive. Here are some of the enhancements we're considering:

1. **Mobile Application**: Developing a mobile app for both iOS and Android to make it even easier for users to access Adopets on the go.

2. **Advanced Search Filters**: Adding more advanced filters such as pet size, temperament, and special needs to help users find their perfect match more efficiently.

3. **Real-time Chat**: Implementing real-time chat functionality to allow instant communication between adopters and pet owners.

4. **Integration with Veterinary Services**: Partnering with local veterinary services to provide health check-ups and vaccinations for pets before adoption.

5. **Adoption Events**: Organizing and promoting local adoption events where users can meet pets in person and interact with other pet lovers.

6. **Pet Training Resources**: Providing a collection of resources and tutorials on pet training and behavior to help new pet owners.

7. **Donation and Sponsorship**: Enabling users to donate or sponsor pets, helping shelters and pet owners cover the costs of pet care.

8. **User Reviews and Ratings**: Allowing users to review and rate their adoption experiences, helping to build trust and improve the platform.

9. **Email Notifications**: Implementing email notifications to keep users informed about their pets, received adoption requests, and updates on adoption request statuses. These notifications will ensure users are always up-to-date with their activities on the platform.


These enhancements will help make the Adopets Platform an even more valuable resource for pet lovers and ensure that every pet finds a loving home.
