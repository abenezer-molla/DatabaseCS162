import {Form, Button, Card} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react';

import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom'

import './App.css';
import {useForm} from 'react-hook-form'

import {Container} from 'react-bootstrap'
import axios from "axios"
import {format} from "date-fns"
import AgentTable from './AgentTable';
import SalesTable from './SalesTable';
import HousesTable from './HousesTable';
import SellerTable from './SellerTable';
import Buyer_Table from './Buyer_Table';
import OfficesTable from './OfficesTable';



function App() {

 

  return (

    <Router>
    <Container className = "d-flex align-item-center justify-content-center" style = {{minHeight:"100vh"}}>
    <div className='w-100' style = {{maxWidth: "400vh"}}>
    <small> Click Here -  <Link to='/agent'>Agent_Table</Link> </small>
    <br></br>
    <small> Click Here -  <Link to='/offices'>Offices_Table</Link> </small>
    <br></br>
    <small> Click Here - <Link to='/buyer'>Buyer_Table</Link> </small>
    <br></br>
    <small> Click Here - <Link to='/seller'>Seller_Table</Link> </small>
    <br></br>
    <small> Click Here - <Link to='/houses'>Houses_Table</Link> </small>
    <br></br>
    <small>Click Here  - <Link to='/sales'>Sales_Table</Link> </small>
    <br></br>
      <Routes>
          <Route exact path="/agent" element={<AgentTable/>}/>
          <Route exact path="/sales" element={<SalesTable/>}/>
          <Route exact path="/houses" element={<HousesTable/>}/>
          <Route exact path="/seller" element={<SellerTable/>}/>
          <Route exact path="/buyer" element={<Buyer_Table/>}/>
          <Route exact path="/offices" element={<OfficesTable/>}/>

      </Routes>
    </div>
    </Container>
  </Router>

  );
}

export default App;
