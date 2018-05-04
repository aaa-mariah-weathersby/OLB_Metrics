import React from 'react';
import PropTypes from 'prop-types';

const Button = (props) => {
  return (
      <button 
      type='button'
      onClick={props.handleClick}
      >
        {props.title}
      </button>
  );
};

Button.propTypes = {
  title: PropTypes.string.isRequired,
  handleClick: PropTypes.func,
};

export default Button;
