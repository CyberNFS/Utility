export function calWindowSize() {
    const windowWidth = window.innerWidth;
    if(windowWidth <= 540){
        return 'xs'
    } else if(windowWidth <= 720){
        return 'md'
    } else if(windowWidth <= 960){
        return 'lg'
    }  else {
        return 'xl'
    }
}