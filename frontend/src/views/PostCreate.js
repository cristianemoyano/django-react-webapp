import React, { Component } from 'react';
import PostService from '../actions/PostService';

const postService = new PostService();




function CustomTextInput({lblTitle, refTitle, lblPost, refPost}) {
    return (
      <div>
        <label>{lblTitle}</label>
        <input
          type="text"
          className="form-control"
          ref={refTitle}
        />

        <label>{lblPost}</label>
        <textarea
          className="form-control"
          ref={refPost}
        >
        </textarea>
      </div>
    );
}


class PostCreate extends Component {
    constructor(props) {
        super(props);

        this.handleSubmit = this.handleSubmit.bind(this);

      }


      handleCreate(){
        postService.createPost(
          {
            "title": this.title.value,
            "post": this.post.value,
        }
        ).then((result)=>{
          alert("Post created!");
        }).catch(()=>{
          alert('There was an error! Please re-check your form.');
        });
      }

      handleSubmit(event) {
        this.handleCreate();

        event.preventDefault();
      }

      render() {
        return (
          <form onSubmit={this.handleSubmit}>
            <div className="form-group">
              <CustomTextInput
                lblTitle='Title'
                refTitle={titleInput => this.title = titleInput}
                lblPost='Post'
                refPost={postInput => this.post = postInput}
              />
              <input className="btn btn-primary" type="submit" value="Publish" />
            </div>
          </form>
        );
      }
}

export default PostCreate;
