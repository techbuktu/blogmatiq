
//Import blogApp's dependent modules
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

//Import all custom modules
import { BlogRoutingModule } from './modules/blog-routing/blog-routing.module';
import { MaterialModule } from './modules/material/material.module';

/* Import the API Services used by blogApp*/
import { CommentService } from './services/comment.service';
import { BlogPostService } from './services/blog-post.service';
import { BloggerService } from './services/blogger.service';
import { BlogCategoryService } from './services/blog-category.service';
import { BlogService } from './services/blog.service';
import { AuthService } from './services/auth.service';

import { AppComponent } from './app.component';
import { BloggerComponent } from './components/blogger/blogger.component';
import { BlogCategoryComponent } from './components/blog-category/blog-category.component';
import { BlogPostComponent } from './components/blog-post/blog-post.component';
import { CommentComponent } from './components/comment/comment.component';
import { BlogListComponent } from './components/blog-list/blog-list.component';
import { BloggerListComponent } from './components/blogger-list/blogger-list.component';
import { CommentListComponent } from './components/comment-list/comment-list.component';
import { HomeComponent } from './components/home/home.component';
import { BlogDetailComponent } from './components/blog-detail/blog-detail.component';
import { BloggerDetailComponent } from './components/blogger-detail/blogger-detail.component';
import { RecentPostsComponent } from './components/recent-posts/recent-posts.component';
import { BlogNavComponent } from './blog-nav/blog-nav.component';
import { LayoutModule } from '@angular/cdk/layout';
import { MatToolbarModule, MatButtonModule, MatSidenavModule, MatIconModule, MatListModule } from '@angular/material';

//Import thirdparty modules 

@NgModule({
  declarations: [
    AppComponent,
    BloggerComponent,
    BlogCategoryComponent,
    BlogPostComponent,
    CommentComponent,
    BlogListComponent,
    BloggerListComponent,
    CommentListComponent,
    HomeComponent,
    BlogDetailComponent,
    BloggerDetailComponent,
    RecentPostsComponent,
    BlogNavComponent
  ],
  imports: [
    BrowserModule, BlogRoutingModule, MaterialModule, 
    BrowserAnimationsModule, HttpClientModule, LayoutModule, MatToolbarModule, MatButtonModule, MatSidenavModule, MatIconModule, MatListModule
  ],
  providers: [
    AuthService, BloggerService, BlogService, 
    BlogCategoryService, BlogPostService, CommentService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
