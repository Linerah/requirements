import React from 'react';
import './Footer.css';
import { Button } from '../../Button';
import { Link } from 'react-router-dom';
import {
  FaGithub,
  // FaInstagram,
  // FaYoutube,
  // FaTwitter,
  FaLinkedin
} from 'react-icons/fa';
import { MdMedication } from 'react-icons/md';

//The Footer has any additional information that can be seen. 
//The footer can also contain external links.

/* The footer is divided in multiple containers and basic HTML tags.
   They vary between some body text, titles, a form, and multiple icons
   which link to their respective sites. 
*/

function Footer() {
  return (
    <div className='footer-container'>
      <section className='footer-subscription'>
        <p className='footer-subscription-heading'>
          Join our mailing list to receive any updates and changes to our platform!
        </p>
        <p className='footer-subscription-text'>
          You can unsubscribe at any time.
        </p>
        <div className='input-areas'>
          <form>
            <input
              className='footer-input'
              name='email'
              type='email'
              placeholder='Your Email'
            />
            <Button buttonStyle='btn--outline'>Join</Button>
          </form>
        </div>
      </section>
      <div className='footer-links'>
        <div className='footer-link-wrapper'>
          <div className='footer-link-items'>
            <h2>About Us</h2>
            <Link to='/sign-up'>How it works</Link>
            <Link to='/'>Testimonials</Link>
            <Link to='/'>Careers</Link>
            <Link to='/'>Terms of Service</Link>
          </div>
          <div className='footer-link-items'>
            <h2>Contact Us</h2>
            <Link to='/'>Contact</Link>
            <Link to='/'>Support</Link>
            <Link to='/'>Destinations</Link>
            <Link to='/'>FAQ's</Link>
          </div>
        </div>
        <div className='footer-link-wrapper'>
          <div className='footer-link-items'>
            <h2>Videos</h2>
            <Link to='/'>Sign-Up Process</Link>
            <Link to='/'>How to Register Your Doctor's Office</Link>
            <Link to='/'>Getting Notified</Link>
          </div>
          <div className='footer-link-items'>
            <h2>Social Media</h2>
            <Link to='/'>Github</Link>
            <Link to='/'>LinkedIn</Link>
          </div>
        </div>
      </div>
      <section className='social-media'>
        <div className='social-media-wrap'>
          <div className='footer-logo'>
            <Link to='/home' className='social-logo'>
            <img src="frontend\src\images\logoOf-removebg-preview.png" className="logo"></img>              
            Gym Scheduler
            </Link>
          </div>
          <small className='website-rights'>Team5 © 2021</small>
          <div className='social-icons'>
            <Link
              className='social-icon-link'
              to='/'
              target='_blank'
              aria-label='Github'
            >
              <FaGithub />
            </Link>
            
            <Link
              className='social-icon-link'
              to='/'
              target='_blank'
              aria-label='LinkedIn'
            >
              <FaLinkedin />
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Footer;