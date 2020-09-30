import axios from 'axios';

export default class PostService{

    getPosts() {
        const url = `/api/v1/posts/`;
        return axios.get(url).then(response => response.data);
    }
    getPostsByURL(link){
        const url = `${link}`;
        return axios.get(url).then(response => response.data);
    }
    getPost(pk) {
        const url = `/api/v1/posts/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    createPost(post){
        const url = `/api/v1/posts/create/`;
        return axios.post(url, post);
    }
}
