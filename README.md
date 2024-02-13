# CookWithUs

Welcome to CookWithUs! This project aims to create a platform where users can share their favorite recipes and engage in real-time communication through posts and direct messages. Whether you're a seasoned chef or a beginner in the kitchen, CookWithUs provides a space for culinary enthusiasts to connect, discover new recipes, and share their cooking experiences.

## Functionality

CookWithUs offers the following key features:

1. **Recipe Sharing**: Users can share their favorite recipes with the community. Each recipe can include ingredients, cooking instructions, preparation time, and any additional notes or tips.

2. **Real-Time Communication**: Users can engage in real-time communication through posts and direct messages. They can discuss recipes, ask questions, share cooking experiences, and connect with other users who have similar culinary interests.

3. **User Profiles**: Each user has a profile where they can showcase their favorite recipes, followers, and following. Users can also customize their profiles with profile pictures and personal information.

4. **Search Functionality**: CookWithUs includes a search feature that allows users to search for recipes based on keywords, ingredients, or categories. This makes it easy for users to discover new recipes and find inspiration for their next culinary adventure.

5. **Notification System**: Users receive notifications for likes, comments, and messages, ensuring that they stay updated on interactions related to their recipes and posts.

## Technologies Used

CookWithUs is built using the following technologies:

- **Frontend**: Django
- **Backend**: Flask
- **Database**: MySQL
- **Real-Time Communication**: Socket.io
<!-- - **Authentication and Authorization**: JSON Web Tokens (JWT) -->
- **Deployment**: AWS

## Getting Started

To run CookWithUs locally, follow these steps:

1. Clone the repository:

```
git clone https://github.com/your-username/CookWithUs.git
```

2. Navigate to the project directory:

```
cd CookWithUs
```

3. Install dependencies:

```
npm install
```

4. Set up environment variables:

   - Create a `.env` file in the root directory.
   - Define the following environment variables in the `.env` file:
     - `MONGODB_URI`: URI for your MongoDB database.
     - `JWT_SECRET`: Secret key for generating JWT tokens.
     - `PORT`: Port number for running the server (optional; default is 5000).

5. Run the server:

```
npm start
```

6. Navigate to the client directory:

```
cd client
```

7. Install client dependencies:

```
npm install
```

8. Run the client:

```
npm start
```

9. Open your browser and visit `http://localhost:3000` to access CookWithUs.

## Contributing

Contributions to CookWithUs are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request. Please ensure that your code follows the project's coding standards and conventions.

## License

This project is licensed under the [MIT License](LICENSE).
