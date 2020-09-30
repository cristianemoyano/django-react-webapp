import React, { Component } from 'react';
import PostService from './PostService';

const postService = new PostService();

class PostCreate extends Component {
    constructor(props) {
        super(props);

        this.handleSubmit = this.handleSubmit.bind(this);
      }

      componentDidMount(){
        const { match: { params } } = this.props;
        if(params && params.pk)
        {
          postService.getPost(params.pk).then((post)=>{
            this.refs.title.value = post.title;
            this.refs.post.value = post.post;
          })
        }
      }

      handleCreate(){
        postService.createPost(
          {
            "title": this.refs.title.value,
            "post": this.refs.post.value,
        }
        ).then((result)=>{
          alert("Post created!");
        }).catch(()=>{
          alert('There was an error! Please re-check your form.');
        });
      }

      handleSubmit(event) {
        const { match: { params } } = this.props;

        this.handleCreate();

        event.preventDefault();
      }

      render() {
        return (
          <form onSubmit={this.handleSubmit}>
          <div className="form-group">

            <label>
              Title:</label>
              <input className="form-control" type="text" ref='title' />

            <label>
              Post:</label>
              <textarea className="form-control" ref='post' ></textarea>

            <input className="btn btn-primary" type="submit" value="Submit" />
            </div>
          </form>
        );
      }
}

export default PostCreate;
