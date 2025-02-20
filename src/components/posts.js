import React, { useEffect, useState } from "react";
import { getPosts } from "../services/api";

const Posts = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const data = await getPosts();
      setPosts(data);
    }
    fetchData();
  }, []);

  return (
    <div>
      <h2>Discussion Forum Posts</h2>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.content} - <b>{post.created_by}</b></li>
        ))}
      </ul>
    </div>
  );
};

export default Posts;
