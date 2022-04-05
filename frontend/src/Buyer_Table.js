import React from 'react'
import {Form, Button, Card} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react';
import {useForm} from 'react-hook-form'


import axios from "axios"
import {format} from "date-fns"

function Buyer_Table() {

    const [eventList, setEventList] = useState([]);
    const {reset}=useForm()
    const [show,setShow]=useState(false)
  
  
  
    useEffect(() => {
      //e.preventDefault();
      // GET request using fetch inside useEffect React hook
      fetch('/buyer')
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
        <h1> Buyer Table</h1>

            {eventList.map(event => {
              return (
                <table>
                <tbody>
                <tr>
                        <th>Buyer ID</th>
                        <th> First Name</th>
                        <th> Last Name</th>
                        <th> Phone Number</th>
                        <th> Email</th>
                        <th>AddressLine1</th>
                        <th>AddressLine2</th>
                        <th>created_at</th>
                    </tr>
                  <tr key = {event.buyer_id} >
                  <td>
                      <h5>{event.buyer_id}</h5>
                    </td>
                    <td>
                      <h5>{event.buyer_firstName}</h5>
                    </td>
                    <td>
                      <h5>{event.buyer_lastName}</h5>
                    </td>
                    <td>
                      <h4>{event.buyer_email}</h4>
                    </td>
                    <td>
                      <p>{event.buyer_phoneNumber}</p>
                    </td>
                    <td>
                      <p>{event.buyer_AddressLine1}</p>
                    </td>
                    <td>
                      <p>{event.buyer_AddressLine2}</p>
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

export default Buyer_Table