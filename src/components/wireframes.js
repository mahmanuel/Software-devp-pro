import React, { useEffect, useState } from "react";
import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:8000/api"; // Django API base URL

const DiscussionForum = () => {
  const [posts, setPosts] = useState([]);
  const [newPost, setNewPost] = useState("");

  useEffect(() => {
    fetchPosts();
  }, []);

  const fetchPosts = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/posts/`);
      setPosts(response.data);
    } catch (error) {
      console.error("Error fetching posts:", error);
    }
  };

  const handleCreatePost = async () => {
    if (!newPost.trim()) return;
    try {
      const response = await axios.post(`${API_BASE_URL}/posts/`, { content: newPost });
      setPosts([response.data, ...posts]);
      setNewPost("");
    } catch (error) {
      console.error("Error creating post:", error);
    }
  };

  return (
    <div>
      <h2>Discussion Forum</h2>
      <div>
        <textarea
          value={newPost}
          onChange={(e) => setNewPost(e.target.value)}
          placeholder="Write a new post..."
        />
        <button onClick={handleCreatePost}>Post</button>
      </div>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.content} - <b>{post.created_by}</b></li>
        ))}
      </ul>
    </div>
  );
};

const ResearchMaterial = () => {
  const [materials, setMaterials] = useState([]);

  useEffect(() => {
    fetchMaterials();
  }, []);

  const fetchMaterials = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/research-materials/`);
      setMaterials(response.data);
    } catch (error) {
      console.error("Error fetching materials:", error);
    }
  };

  return (
    <div>
      <h2>Research Material</h2>
      <ul>
        {materials.map((material) => (
          <li key={material.id}>{material.title}</li>
        ))}
      </ul>
    </div>
  );
};

const MentorshipProgram = () => {
  const [mentors, setMentors] = useState([]);

  useEffect(() => {
    fetchMentors();
  }, []);

  const fetchMentors = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/mentors/`);
      setMentors(response.data);
    } catch (error) {
      console.error("Error fetching mentors:", error);
    }
  };

  return (
    <div>
      <h2>Mentorship Program</h2>
      <ul>
        {mentors.map((mentor) => (
          <li key={mentor.id}>{mentor.name} - {mentor.expertise}</li>
        ))}
      </ul>
    </div>
  );
};

const EventAnnouncements = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetchEvents();
  }, []);

  const fetchEvents = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/events/`);
      setEvents(response.data);
    } catch (error) {
      console.error("Error fetching events:", error);
    }
  };

  return (
    <div>
      <h2>Event Announcements</h2>
      <ul>
        {events.map((event) => (
          <li key={event.id}>{event.title} - {event.date}</li>
        ))}
      </ul>
    </div>
  );
};

const AITSApp = () => {
  return (
    <div>
      <DiscussionForum />
      <ResearchMaterial />
      <MentorshipProgram />
      <EventAnnouncements />
    </div>
  );
};

export default AITSApp;
