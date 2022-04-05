import React from 'react'
import {Form, Button, Card} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react';
import {useForm} from 'react-hook-form'


import axios from "axios"
import {format} from "date-fns"

function SellerTable() {

    const [eventList, setEventList] = useState([]);
    const {reset}=useForm()
    const [show,setShow]=useState(false)
  
  
  
    useEffect(() => {
      //e.preventDefault();
      // GET request using fetch inside useEffect React hook
      fetch('/seller')
          .then(response => response.json())
          .then(data => {
            setEventList(data.event)
            console.log("LOOK HERE", data.event)
          }
  
          )   
  
  // empty dependency array means this effect will only run once (like componentDidMount in classes)
  }, []);
  return (
    <div className='stock-container'>
    
    <Card>

        <section>

         <h1> Seller Table</h1>

            {eventList.map(event => {
              return (
                <table>
                <tbody>
                <tr>
                        <th>Seller ID</th>
                        <th> First Name</th>
                        <th> Last Name</th>
                        <th> Email</th>
                        <th> Phone Number</th>
                        <th>AddressLine1</th>
                        <th>AddressLine2</th>
                        <th>created_at</th>
                    </tr>
                  <tr key = {event.seller_id} >
                   <td>
                      <h5>{event.seller_id}</h5>
                    </td>
                    <td>
                      <h5>{event.seller_firstName}</h5>
                    </td>
                    <td>
                      <h5>{event.seller_lastName}</h5>
                    </td>
                    <td>
                      <h4>{event.email}</h4>
                    </td>
                    <td>
                      <p>{event.phoneNumber}</p>
                    </td>
                    <td>
                      <p>{event.AddressLine1}</p>
                    </td>
                    <td>
                      <p>{event.AddressLine2}</p>
                    </td>
                    <td>
                      <p>{event.created_at}</p>
                    </td>
                  </tr>
                </tbody>
              </table>
               
         

              )
            })}

      
        </section>

    </Card>

    </div>
  )
}

export default SellerTable