import  React from  'react';

import { Route } from  'react-router-dom'
import  PostList  from  '../views/PostList'
import  PostCreate  from  '../views/PostCreate'

const  BaseLayout  = () => (
<div  className="container-fluid">
    <nav  className="navbar navbar-expand-lg navbar-light bg-light">
        <a  className="navbar-brand"  href="/">React Blog</a>
        <button  className="navbar-toggler"  type="button"  data-toggle="collapse"  data-target="#navbarNavAltMarkup"  aria-controls="navbarNavAltMarkup"  aria-expanded="false"  aria-label="Toggle navigation">
        <span  className="navbar-toggler-icon"></span>
    </button>
    <div  className="collapse navbar-collapse"  id="navbarNavAltMarkup">
        <div  className="navbar-nav">
            <a  className="nav-item nav-link"  href="/create">Create</a>
        </div>
    </div>
    </nav>
    <div  className="content">
        <Route  path="/"  exact  component={PostList}  />
        <Route  path="/create/"  exact  component={PostCreate}  />
    </div>
</div>
)

export  default  BaseLayout;
