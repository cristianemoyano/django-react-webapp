import  React, { Component } from  'react';
import  PostService  from  './PostService';

const  postService  =  new  PostService();

class  PostsList  extends  Component {

constructor(props) {
    super(props);
    this.state  = {
        posts: [],
        nextPageURL:  ''
    };
    this.nextPage  =  this.nextPage.bind(this);
}

componentDidMount() {
    var  self  =  this;
    postService.getPosts().then(function (result) {
        console.log(result);
        self.setState({ posts:  result.data, nextPageURL:  result.nextlink})
    });
}


nextPage(){
    var  self  =  this;
    console.log(this.state.nextPageURL);
    postService.getPostsByURL(this.state.nextPageURL).then((result) => {
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
                <button  onClick={(e)=>  this.handleDelete(e,post.pk) }> Delete</button>
                <a  href={"/posts/" + post.pk}> Update</a>
                </td>
            </tr>)}
            </tbody>
            </table>
            <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
        </div>
        );
  }
}
export  default  PostsList;
