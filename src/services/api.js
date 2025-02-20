import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api"; // Django API base URL

// Axios instance with default settings
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Fetch users
export const getUsers = async () => {
  try {
    const response = await api.get("/users/");
    return response.data;
  } catch (error) {
    console.error("Error fetching users:", error);
  }
};

// Fetch posts from the discussion forum
export const getPosts = async () => {
  try {
    const response = await api.get("/posts/");
    return response.data;
  } catch (error) {
    console.error("Error fetching posts:", error);
  }
};

// Create a new post
export const createPost = async (postData) => {
  try {
    const response = await api.post("/posts/", postData);
    return response.data;
  } catch (error) {
    console.error("Error creating post:", error);
  }
};

const token = localStorage.getItem("token"); // Assuming token is stored in localStorage

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
    Authorization: `Token ${token}`, // Add token for authenticated requests
  },
});
