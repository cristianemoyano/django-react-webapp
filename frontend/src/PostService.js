import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class PostService{

    constructor(){}


    getPosts() {
        const url = `${API_URL}/api/v1/posts/`;
        return axios.get(url).then(response => response.data);
    }
    getPostsByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getPost(pk) {
        const url = `${API_URL}/api/v1/posts/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    createPost(post){
        const url = `${API_URL}/api/v1/posts/`;
        return axios.post(url, post);
    }
}
