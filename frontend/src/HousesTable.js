import React from 'react'
import {Form, Button, Card} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react';
import {useForm} from 'react-hook-form'


import axios from "axios"
import {format} from "date-fns"

function HousesTable() {

    const [eventList, setEventList] = useState([]);
    const {reset}=useForm()
    const [show,setShow]=useState(false)
  
  
  
    useEffect(() => {
      //e.preventDefault();
      // GET request using fetch inside useEffect React hook
      fetch('/houses')
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
        <h1> Houses Table</h1>

            {eventList.map(event => {
              return (
                <table>
                <tbody>
                <tr>
                        <th>House ID</th>
                        <th> Zip Code</th>
                        <th>AddressLine1</th>
                        <th> Area in Square Meter</th>
                        <th> Price in USD</th>
                        <th> Date of Listing</th>
                        <th>created_at</th>
                    </tr>   
                  <tr key = {event.house_id} >
                  <td>
                      <h5>{event.house_id}</h5>
                    </td>
                    <td>
                      <h5>{event.zipCode}</h5>
                    </td>
                    <td>
                      <h5>{event.AddressLine1}</h5>
                    </td>
                    <td>
                      <p>{event.area_in_square_meter}</p>
                    </td>
                    <td>
                      <h4>{event.house_price}</h4>
                    </td>

                    <td>
                      <p>{event.date_of_listing}</p>
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

export default HousesTable