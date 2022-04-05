import React from 'react'
import {Form, Button, Card} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react';
import {useForm} from 'react-hook-form'


import axios from "axios"
import {format} from "date-fns"

function Offices_Table() {

    const [eventList, setEventList] = useState([]);
    const {reset}=useForm()
    const [show,setShow]=useState(false)
  
  
  
    useEffect(() => {
      //e.preventDefault();
      // GET request using fetch inside useEffect React hook
      fetch('/offices')
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
        <h1> Offices Table</h1>

            {eventList.map(event => {
              return (
                <table>
                <tbody>
                    <tr>
                        <th>Name</th>
                        <th>Phone Number</th>
                        <th>AddressLine1</th>
                        <th>AddressLine2</th>
                        <th>created_at</th>
                    </tr>
                  <tr key = {event.office_id} >
                    <td>
                      <h5>{event.office_name}</h5>
                    </td>
                    <td>
                      <h5>{event.office_phoneNumber}</h5>
                    </td>
                    <td>
                      <p>{event.office_addressLine1}</p>
                    </td>
                    <td>
                      <p>{event.office_addressLine2}</p>
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

export default Offices_Table