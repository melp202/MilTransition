import React, { Component } from 'react';
import ReactDom from 'react-dom';

// Import Components
import Header from './layout/Header';
import States from './transitioning/States';

class App extends Component {
	render() {
		return (
			<div>
				<Header />
				<div className="container">
					<States />
				</div>
			</div>
		);
	}
}

ReactDom.render(<App />, document.getElementById('app'));
