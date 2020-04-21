import React from 'react'
import image from '../images/images.jpeg'


class MentorProfile extends React.Component {
  constructor() {
    super()
    this.state = {

    }
  }


  render() {
    console.log('render')
    return <div id="container-mentor-profile"  >
      <div className="img-background"  style={{ backgroundImage: `url(${image})` }}></div>
      <div className="opacity">
        <div id="content-mentor-profile">
          <div className="left-container">

            <div className="photo" style={{ backgroundImage: `url(${'http://localhost:4000/' + 'photo' })` }} >Photo</div>
            <div className="votes">Votes <br/></div>
          </div>

          <div className="right-content">
            
            <h3>Name</h3>
            <p>Long description <br />
              <br/>               
              Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Molestias, similique. Quidem possimus aliquid animi hic.
              Reprehenderit, impedit. Sed deserunt recusandae fuga pariatur
              dolores possimus id perspiciatis quam commodi, dolorum harum
              voluptatibus voluptatem esse quidem at cum provident inventore
              consectetur consequuntur laudantium reprehenderit cumque
              molestiae delectus eius? Excepturi aliquam odio veniam.
            </p>
            <div className="skill"> <h4>Skills:</h4>  
              
              <h5>Date</h5>
            
            </div>
          
        </div>
        </div>
      </div>
    </div>
  }


}



export default MentorProfile