# Testing

## Validation

### CSS

### JS

### Python

## Lighthouse

### Mobile

### Desktop

## Test Types

### Manual Testing

### Automated Testing

## Bugs

### Development Bugs

#### CSRF Trusted origins 
1. When trying to sign in, sign out or register the following error appears:
Forbidden (403)
CSRF verification failed. Request aborted.
2. Added a CSRF_TRUSTED_ORIGINS witht the gitpod server url
3. All auth functionality now working as expected, this was not required for Heroku

#### Newsletter email not appearing in admin once signed up
1. When creating the newsletter signup the terminal messages gave a 200 response which means the post request should have worked however the email address did not appear in the admin.

### Unfixed bugs

#### Basket does not show in account pages
1. When a user adds a product to their basket it shows the quantity next to the basket icon, but on the account pages the number is not shown

