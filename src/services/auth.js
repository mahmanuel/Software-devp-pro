import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api";

export const login = async (username, password) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/login/`, { username, password });
    localStorage.setItem("token", response.data.token);
    return response.data;
  } catch (error) {
    console.error("Login failed", error);
  }
};

export const logout = async () => {
  const token = localStorage.getItem("token");
  try {
    await axios.post(`${API_BASE_URL}/logout/`, {}, {
      headers: { Authorization: `Token ${token}` }
    });
    localStorage.removeItem("token");
  } catch (error) {
    console.error("Logout failed", error);
  }
};

export const getUserProfile = async () => {
  const token = localStorage.getItem("token");
  try {
    const response = await axios.get(`${API_BASE_URL}/profile/`, {
      headers: { Authorization: `Token ${token}` }
    });
    return response.data;
  } catch (error) {
    console.error("Failed to fetch profile", error);
  }
};
