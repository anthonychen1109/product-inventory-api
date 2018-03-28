import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      products: {
        id: '',
        name: '',
        quantity_on_hand: ''
      }
    };
    this.getProducts = this.getProducts.bind(this);
  }

  // componentDidMount() {
  //   axios.get('http://127.0.0.1:8000/products/')
  //     .then(response => this.setState({ products: response.data }));
  // }

  getProducts() {
    axios.get('http://127.0.0.1:8000/products/')
      .then(response => this.setState({
        products: {...this.state.products,
          id: response.data[0].id,
          name: response.data[0].name,
          quantity_on_hand: response.data[0].quantity_on_hand
        },
      }));
  }

  render() {
    console.log(this.state.products);
    return (
      <div>
        <button
          onClick={this.getProducts}
          >
          Get Data
        </button>
      </div>
    )
  }
}

export default App;
