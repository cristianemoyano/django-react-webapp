import  React, { Component } from  'react';
import  PostService  from  '../actions/PostService';

const  postService  =  new  PostService();

class  PostsList  extends  Component {

constructor(props) {
    super(props);
    this.state  = {
        posts: [],
        nextPageURL:  ''
    };
}

componentDidMount() {
    var  self  =  this;
    postService.getPosts().then(function (result) {
        console.log(result);
        self.setState({ posts:  result.data, nextPageURL:  result.nextlink})
    });
}


render() {

    return (
        <div  className="customers--list">
            <table  className="table">
            <thead  key="thead">
            <tr>
                <th>#</th>
                <th>Title</th>
                <th>Post</th>
            </tr>
            </thead>
            <tbody>
            {this.state.posts.map( post  =>
                <tr  key={post.pk}>
                <td>{post.pk}  </td>
                <td>{post.title}</td>
                <td>{post.post}</td>
                <td>
                </td>
            </tr>)}
            </tbody>
            </table>
        </div>
        );
  }
}
export  default  PostsList;
